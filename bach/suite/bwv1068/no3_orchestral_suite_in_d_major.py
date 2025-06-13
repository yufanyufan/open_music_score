with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Air')
    with Identification():
        Creator('Johann Sebastian Bach (1685–1750)', type='composer')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(4.57416)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2444.0)
            PageWidth(1888.0)
            with PageMargins(type='both'):
                LeftMargin(86.9998)
                RightMargin(86.9998)
                TopMargin(86.9998)
                BottomMargin(86.9998)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='Times New Roman', font_size='7.4925')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685–1750)\n', default_x=1801.0, default_y=2322.0, justify='right', valign='bottom', font_family='Times New Roman', font_size='7.1887')
        CreditWords('Arr. for winds by Luis F. Acosta')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Air', default_x=943.998, default_y=2361.06, justify='center', valign='top', font_family='Times New Roman', font_size='14.3775')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Oboe')
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
            PartName("Oboe d'amore")
            PartAbbreviation("Ob. d'a.")
            with ScoreInstrument(id='P2-I1'):
                InstrumentName("Oboe d'amore")
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(69)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('English Horn')
            PartAbbreviation('E. Hn.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('English Horn')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(70)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Bassoon')
            PartAbbreviation('Bsn.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(71)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=373.43):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(149.21)
                        RightMargin(0.0)
                    TopSystemDistance(106.42)
            with Attributes():
                Divisions(8.0)
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
                    with Metronome(parentheses='no', default_x=-39.32, relative_x=-29.62, relative_y=46.75):
                        BeatUnit('eighth')
                        PerMinute('65')
                Sound(tempo=32.5)
            with Note(default_x=118.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=341.57):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=49.48, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=72.91, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=96.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=119.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=190.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=265.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='3', width=438.67):
            with Note(default_x=15.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=213.53, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=240.99, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=269.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=297.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=324.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=354.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=382.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=409.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='4', width=411.13):
            with Note(default_x=15.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=207.61, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=232.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=283.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=308.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=333.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=359.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=384.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=481.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.36)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=98.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=212.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=240.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=268.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=306.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=323.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=341.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=369.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=396.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=424.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=452.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='6', width=458.57):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=86.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=104.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=133.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=172.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=200.67, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=228.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=294.22):
            with Note(default_x=15.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='8', width=390.05):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=53.92, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=80.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.53, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=115.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=304.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='9', width=521.57):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.36)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=97.35, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=295.98, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=323.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=379.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=407.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=437.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=464.89, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=492.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='10', width=438.51):
            with Note(default_x=15.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=220.96, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=247.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=274.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=301.94, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=328.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=355.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=382.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=409.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=373.18):
            with Note(default_x=12.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=120.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=146.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=172.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=208.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=224.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=241.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=267.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=293.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=345.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=291.39):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=86.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=104.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=133.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=172.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=200.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=228.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='13', width=500.26):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.36)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=126.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=191.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=214.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=230.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=245.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=261.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=277.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=300.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=446.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
        with Measure(number='14', width=417.46):
            with Note(default_x=21.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.61, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=125.29, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=150.08, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.87, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=224.45, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=292.62, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=308.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=323.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=339.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=366.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=391.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='15', width=382.58):
            with Note(default_x=17.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=43.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=66.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=133.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=155.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=200.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=229.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=251.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=300.54, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=345.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='16', width=324.34):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=123.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=139.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=155.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=199.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='17', width=481.75):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.36)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=97.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=176.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=206.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=256.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=280.95, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=371.92, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=425.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=455.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='18', width=357.16):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=31.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=47.13, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=69.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=101.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=155.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=171.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=186.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=241.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=263.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='19', width=409.21):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=162.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=188.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=213.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=356.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=382.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=376.53):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=145.55, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=168.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=191.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='21', width=541.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.36)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=97.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=208.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=236.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.22, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=320.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=347.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=375.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=433.31, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=471.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=499.3, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=516.67, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='22', width=329.49):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=83.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=106.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.53, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.2, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=184.46, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=292.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='23', width=429.94):
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=64.93, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=166.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=217.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=268.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=294.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=310.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Tie(type='start')
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tied(type='start')
            with Note(default_x=326.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=351.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=402.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='24', width=323.77):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=50.17)
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=29.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=47.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=105.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=133.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=191.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=226.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=243.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='25', width=720.7):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(89.36)
                        RightMargin(903.94)
                    SystemDistance(150.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('rit.', relative_y=40.0)
            with Note(default_x=97.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=135.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=172.74, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=292.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=352.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=472.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=546.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=583.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=373.43):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(-2)
                    Chromatic(-3.0)
            with Note(default_x=118.77, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=341.57):
            with Note(default_x=12.0, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=96.34, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=189.68, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='3', width=438.67):
            with Note(default_x=15.8, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.74, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=87.2, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.66, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=158.6, default_y=-90.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.07, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=213.17, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='4', width=411.13):
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.18, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.42, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.66, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.9, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.14, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=182.38, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=207.25, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='5', width=481.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=97.72, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=268.29, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=306.5, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=341.24, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=369.03, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=424.61, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=458.57):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=68.96, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=172.19, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=228.79, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=294.22):
            with Note(default_x=15.32, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(32.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='8', width=390.05):
            with Note(default_x=12.0, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=115.98, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=220.41, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='9', width=521.57):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=97.72, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=141.77, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=169.31, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=196.85, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=240.91, default_y=-90.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=268.44, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=295.62, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='10', width=438.51):
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.99, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.99, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.98, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.97, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.97, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.96, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.6, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='11', width=373.18):
            with Note(default_x=12.36, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=172.58, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=208.46, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=241.08, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=267.18, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=319.38, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=291.39):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=68.98, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=172.26, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=228.88, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='13', width=500.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=126.31, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=300.5, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=323.91, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=352.77, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=399.58, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=422.98, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=446.39, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=475.25, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=417.46):
            with Note(default_x=21.03, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=174.87, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=224.09, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='15', width=382.58):
            with Note(default_x=16.87, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=200.31, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=229.18, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.53, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.87, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=300.54, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=322.88, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=345.23, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='16', width=324.34):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.71, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=101.41, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=155.1, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=199.44, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='17', width=481.75):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=97.72, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=176.86, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=280.95, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=320.52, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=345.25, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=371.92, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=400.79, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=425.52, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=357.16):
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=69.96, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=132.72, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
            with Note(default_x=186.52, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='19', width=409.21):
            with Note(default_x=15.8, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=56.4, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.27, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.65, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.31, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=162.69, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=213.45, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=254.05, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=279.43, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=304.81, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=331.47, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=356.85, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='20', width=376.53):
            with Note(default_x=17.23, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=53.89, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=76.81, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=99.72, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=122.63, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=145.55, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=191.37, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=214.29, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.2, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.11, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=283.03, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=541.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.17)
            with Note(default_x=97.72, default_y=-170.17):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=125.5, default_y=-180.17):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.29, default_y=-170.17):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.08, default_y=-155.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=208.86, default_y=-145.17):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=264.43, default_y=-155.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=320.01, default_y=-155.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=375.58, default_y=-145.17):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=404.45, default_y=-140.17):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=433.31, default_y=-175.17):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='22', width=329.49):
            with Note(default_x=12.0, default_y=-175.17):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.86, default_y=-170.17):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=83.71, default_y=-165.17):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=184.1, default_y=-160.17):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='23', width=429.94):
            with Note(default_x=14.0, default_y=-160.17):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.93, default_y=-150.17):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=115.86, default_y=-135.17):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=217.72, default_y=-135.17):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=243.19, default_y=-140.17):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=268.65, default_y=-145.17):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.12, default_y=-150.17):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=326.48, default_y=-155.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=377.41, default_y=-150.17):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='24', width=323.77):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=50.17)
            with Note(default_x=12.0, default_y=-155.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=133.93, default_y=-160.17):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=162.61, default_y=-165.17):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=191.3, default_y=-160.17):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=243.85, default_y=-165.17):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='25', width=720.7):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(79.17)
            with Note(default_x=97.72, default_y=-139.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=352.81, default_y=-144.17):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=412.83, default_y=-149.17):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=472.85, default_y=-144.17):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=583.2, default_y=-149.17):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=373.43):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(-4)
                    Chromatic(-7.0)
            with Note(default_x=121.73, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=246.6, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=341.57):
            with Note(default_x=12.0, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=96.34, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=189.68, default_y=-235.0):
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
        with Measure(number='3', width=438.67):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.74, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=158.6, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=213.17, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='4', width=411.13):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=56.18, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=157.14, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=207.25, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='5', width=481.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=98.08, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=212.71, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=268.29, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=306.5, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=369.03, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=424.61, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='6', width=458.57):
            with Note(default_x=12.0, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=68.96, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=133.03, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=172.19, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=228.79, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='7', width=294.22):
            with Note(default_x=18.28, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=155.27, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='8', width=390.05):
            with Note(default_x=12.0, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=115.98, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=220.41, default_y=-235.0):
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
        with Measure(number='9', width=521.57):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=97.72, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=141.77, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=240.91, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=295.62, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='10', width=438.51):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=58.99, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=166.97, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=220.6, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='11', width=373.18):
            with Note(default_x=12.72, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=120.38, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=172.58, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=208.46, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=267.18, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=319.38, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='12', width=291.39):
            with Note(default_x=12.0, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=68.98, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=133.09, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=172.26, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=228.88, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='13', width=500.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=126.31, default_y=-235.0):
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
            with Note(default_x=300.5, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=352.77, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=376.18, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=399.58, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='14', width=417.46):
            with Note(default_x=21.03, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=45.82, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.61, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.4, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=125.29, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=174.87, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=224.45, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=292.62, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=382.58):
            with Note(default_x=17.23, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=43.9, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.24, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.59, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=110.93, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=133.28, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.62, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.97, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=200.31, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=251.53, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=273.87, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=300.54, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=345.23, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='16', width=324.34):
            with Note(default_x=12.0, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.71, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=79.06, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.41, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=155.1, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.45, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=199.44, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='17', width=481.75):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=97.72, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=137.29, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=176.86, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=206.75, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=231.49, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=280.95, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=345.25, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=371.92, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=357.16):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=69.96, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=101.34, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=132.72, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=186.88, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=241.09, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=263.92, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=286.74, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=309.57, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=332.39, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=409.21):
            with Note(default_x=15.8, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=56.4, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=162.69, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=213.45, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=254.05, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=356.85, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='20', width=376.53):
            with Note(default_x=17.23, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=53.89, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=145.55, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=191.37, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=283.03, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=305.94, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.85, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=351.77, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=541.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=97.72, default_y=-250.17):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.29, default_y=-255.17):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=208.86, default_y=-260.17):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=264.43, default_y=-265.17):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=320.01, default_y=-270.17):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=433.31, default_y=-250.17):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='22', width=329.49):
            with Note(default_x=12.0, default_y=-250.17):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.86, default_y=-255.17):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=83.71, default_y=-250.17):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=184.1, default_y=-270.17):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='23', width=429.94):
            with Note(default_x=14.0, default_y=-265.17):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=39.47, default_y=-280.17):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.93, default_y=-265.17):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.4, default_y=-255.17):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=115.86, default_y=-245.17):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=141.33, default_y=-250.17):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.79, default_y=-255.17):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.26, default_y=-260.17):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=217.72, default_y=-265.17):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=268.65, default_y=-250.17):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=377.41, default_y=-255.17):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='24', width=323.77):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=50.17)
            with Note(default_x=12.0, default_y=-260.17):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=133.93, default_y=-265.17):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=191.3, default_y=-285.17):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=243.85, default_y=-285.17):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='25', width=720.7):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=97.72, default_y=-244.17):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=352.81, default_y=-249.17):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=472.85, default_y=-269.17):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=583.2, default_y=-269.17):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=373.43):
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
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=122.09, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.31, default_y=-305.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=184.53, default_y=-310.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=215.74, default_y=-345.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=246.96, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=278.18, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=309.39, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=340.61, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=341.57):
            with Note(default_x=12.0, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=49.48, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=96.34, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=143.19, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=190.04, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=227.52, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=265.01, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=302.49, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='3', width=438.67):
            with Note(default_x=15.8, default_y=-365.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.74, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=114.66, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=158.6, default_y=-370.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=213.53, default_y=-375.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=269.86, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=324.78, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=382.14, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='4', width=411.13):
            with Note(default_x=15.8, default_y=-370.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.18, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=106.66, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=157.14, default_y=-375.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=207.61, default_y=-380.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=258.09, default_y=-345.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=308.57, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=359.05, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=481.79):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=98.08, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=136.29, default_y=-305.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=174.5, default_y=-310.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=212.71, default_y=-345.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=268.29, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=306.5, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=369.03, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=424.61, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=458.57):
            with Note(default_x=12.0, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=68.96, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=133.03, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=172.19, default_y=-370.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=229.15, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=257.62, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.1, default_y=-345.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.58, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=343.06, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=371.54, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=400.02, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=428.49, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='7', width=294.22):
            with Note(default_x=18.64, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=52.89, default_y=-305.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=87.14, default_y=-310.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=121.38, default_y=-345.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=155.63, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=189.88, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=224.13, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=258.38, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=390.05):
            with Note(default_x=12.0, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.92, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=115.98, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=168.38, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=220.77, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=262.69, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=304.61, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=346.53, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='9', width=521.57):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=97.72, default_y=-365.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=141.77, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=196.85, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=240.91, default_y=-370.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=295.98, default_y=-375.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=352.38, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=407.46, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=464.89, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='10', width=438.51):
            with Note(default_x=15.8, default_y=-370.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=58.99, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=112.98, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=166.97, default_y=-375.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=220.96, default_y=-380.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=274.94, default_y=-345.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=328.93, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=382.92, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='11', width=373.18):
            with Note(default_x=12.72, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.61, default_y=-305.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=84.49, default_y=-310.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=120.38, default_y=-345.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=172.58, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=208.46, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=267.18, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=319.38, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=291.39):
            with Note(default_x=12.0, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=68.98, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=133.09, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=172.26, default_y=-370.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=228.88, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='13', width=500.26):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=126.67, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=158.85, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=191.03, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=245.77, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=300.5, default_y=-365.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=352.77, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=399.58, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=446.39, default_y=-370.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='14', width=417.46):
            with Note(default_x=21.03, default_y=-375.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=70.61, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=125.29, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=174.87, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=224.45, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=258.53, default_y=-300.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=292.62, default_y=-305.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=366.28, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=382.58):
            with Note(default_x=17.23, default_y=-345.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.24, default_y=-310.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=110.93, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=155.62, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=200.31, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=251.53, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=300.54, default_y=-345.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=345.23, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='16', width=324.34):
            with Note(default_x=12.0, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.71, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=101.41, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=155.1, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=199.8, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=230.54, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=261.27, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=292.01, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='17', width=481.75):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=97.72, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=137.29, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=176.86, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=231.49, default_y=-365.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=280.95, default_y=-370.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=320.52, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=371.92, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=425.52, default_y=-375.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='18', width=357.16):
            with Note(default_x=15.8, default_y=-380.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=69.96, default_y=-345.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=101.34, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=132.72, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=186.88, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=218.27, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=263.92, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=309.57, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='19', width=409.21):
            with Note(default_x=15.8, default_y=-365.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.4, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=110.65, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=162.69, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=213.45, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=254.05, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=304.81, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=356.85, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='20', width=376.53):
            with Note(default_x=17.23, default_y=-355.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.89, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=99.72, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=145.55, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=191.37, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=237.2, default_y=-300.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=283.03, default_y=-305.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=328.85, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=541.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=97.72, default_y=-375.17):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=153.29, default_y=-340.17):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=208.86, default_y=-350.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=264.43, default_y=-340.17):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=320.01, default_y=-335.17):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=375.58, default_y=-370.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=433.31, default_y=-375.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=471.52, default_y=-340.17):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=329.49):
            with Note(default_x=12.0, default_y=-345.17):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.86, default_y=-380.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=83.71, default_y=-385.17):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=128.53, default_y=-350.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=184.46, default_y=-355.17):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=220.32, default_y=-390.17):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=256.18, default_y=-395.17):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=292.03, default_y=-360.17):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='23', width=429.94):
            with Note(default_x=14.0, default_y=-365.17):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=64.93, default_y=-400.17):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=115.86, default_y=-405.17):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=166.79, default_y=-370.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=217.72, default_y=-375.17):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=268.65, default_y=-385.17):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=326.48, default_y=-370.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=377.41, default_y=-355.17):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=323.77):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=50.17)
            with Note(default_x=12.0, default_y=-350.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.55, default_y=-355.17):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=133.93, default_y=-350.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=191.3, default_y=-385.17):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=243.85, default_y=-405.17):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='25', width=720.7):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=97.72, default_y=-334.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=232.77, default_y=-339.17):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=352.81, default_y=-334.17):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=472.85, default_y=-369.17):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=583.2, default_y=-389.17):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')