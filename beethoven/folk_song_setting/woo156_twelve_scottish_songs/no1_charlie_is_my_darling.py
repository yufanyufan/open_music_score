with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Charlie is my darling')
    with Identification():
        Creator('Ludwig van Beethoven', type='composer')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-14')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
        Source('http://musescore.com/user/3099636/scores/6187668')
    with Defaults():
        with Scaling():
            Millimeters(5.456)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2176.91)
            PageWidth(1540.03)
            with PageMargins(type='even'):
                LeftMargin(73.3138)
                RightMargin(73.3138)
                TopMargin(73.3138)
                BottomMargin(146.628)
            with PageMargins(type='odd'):
                LeftMargin(73.3138)
                RightMargin(73.3138)
                TopMargin(73.3138)
                BottomMargin(146.628)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Charlie is my darling', default_x=770.015, default_y=2103.6, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Schottisches Volkslied', default_x=770.015, default_y=2030.29, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Ludwig van Beethoven', default_x=1466.72, default_y=2003.6, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Fiolin')
            PartAbbreviation('Fio.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Fiolin')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(6)
                MidiProgram(41)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Cello')
            PartAbbreviation('Vc.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Cello')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(9)
                MidiProgram(43)
                Volume(78.7402)
                Pan(0.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P3'):
            PartName('Sopran 1')
            PartAbbreviation('S1.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Sopran')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Sopran 2')
            PartAbbreviation('S2.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Sopran')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('Tenor')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P6'):
            PartName('Bass')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P7'):
            PartName('Piano')
            with ScoreInstrument(id='P7-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P7-I1', port=1)
            with MidiInstrument(id='P7-I1'):
                MidiChannel(5)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=144.26):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(87.56)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Allegretto con anima', default_x=-36.12, default_y=18.36, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=86.0)
            with Note(default_x=99.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=99.95, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='1', width=175.15):
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=15.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=131.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.15, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='2', width=175.15):
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=15.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=131.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=131.15, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='3', width=176.77):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=54.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=54.72, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=93.63, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.63, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=132.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=132.55, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
        with Measure(number='4', width=190.8):
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=65.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=65.75, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=105.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=105.87, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=145.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=145.98, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='5', width=202.9):
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=58.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=151.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=178.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='6', width=94.64):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=33.35, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=68.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=68.45, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='7', width=146.18):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=3.26, relative_y=30.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=98.15, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=121.41, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=175.12):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(67.38)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=80.65, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=104.81, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=120.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='9', width=58.04):
            with Direction(placement='above'):
                with DirectionType():
                    Segno(default_x=-8.02, relative_y=20.0)
                Sound(segno='segno')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=30.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=33.27, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=178.92):
            with Note(default_x=26.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=56.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=115.08, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='11', width=234.03):
            with Note(default_x=19.38, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=137.66, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=199.63, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
        with Measure(number='12', width=189.76):
            with Note(default_x=19.38, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=106.11, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=155.36, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
        with Measure(number='13', width=260.89):
            with Note(default_x=17.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=141.7, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='14', width=229.27):
            with Note(default_x=26.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=56.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.31, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=130.61, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=154.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.4, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='15', width=214.92):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(67.38)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=82.58, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=113.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=143.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=180.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='16', width=165.85):
            with Note(default_x=32.06, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=86.89, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=131.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='17', width=193.91):
            with Note(default_x=20.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=135.67, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='18', width=224.3):
            with Note(default_x=22.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=50.56, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=78.33, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='19', width=274.76):
            with Note(default_x=24.45, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='20', width=252.28):
            with Note(default_x=21.92, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='21', width=235.97):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(67.38)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=82.58, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=166.9, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=200.64, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=263.46):
            with Note(default_x=26.88, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=72.13, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='23', width=254.96):
            with Note(default_x=15.56, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=80.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='24', width=227.05):
            with Note(default_x=32.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=182.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=182.16, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
        with Measure(number='25', width=164.17):
            with Note(default_x=20.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=53.66, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=129.06, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
        with Measure(number='26', width=180.42):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=134.47, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='27', width=255.15):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(67.38)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=114.95, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=137.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=162.78, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=185.32, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=207.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=230.39, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=167.92):
            with Note(default_x=19.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='29', width=156.37):
            with Note(default_x=19.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.68, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='30', width=151.52):
            with Note(default_x=17.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=108.14, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=253.15):
            with Note(default_x=26.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=56.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.02, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=138.13, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=170.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.32, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=153.43):
            with Note(default_x=19.38, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.93, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=119.05, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='33', width=188.47):
            with Note(default_x=32.06, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=107.29, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=156.2, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='34', width=217.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(67.38)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=82.58, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='35', width=189.68):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=240.86):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=15.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=123.32, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=123.32, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=212.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='37', width=167.92):
            with Note(default_x=15.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=109.45, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=143.15, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='38', width=122.54):
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='39', width=58.6):
            with Direction(placement='above'):
                with DirectionType():
                    Segno(default_x=-8.02, relative_y=20.0)
                Sound(segno='segno')
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='40', width=151.64):
            with Note(default_x=21.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=21.03, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=117.26, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=117.26, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='41', width=177.46):
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=15.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=133.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=133.75, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='42', width=430.11):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(67.38)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=94.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=94.62, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=337.84, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=337.84, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='43', width=358.24):
            with Attributes():
                with Key():
                    Fifths(2)
            with Note(default_x=38.63, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=38.63, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=34.33)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=34.33)
            with Note(default_x=109.3, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=153.47, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=197.63, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=268.3, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=312.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Dashes(type='stop', number=1)
        with Measure(number='44', width=331.23):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=4.33, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=85.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=129.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=172.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=242.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=286.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='45', width=206.44):
            with Note(default_x=15.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=13.4, relative_y=10.0)
            with Note(default_x=15.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='0', implicit='yes', width=144.26):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=99.95, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='1', width=175.15):
            with Note(default_x=15.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=54.25, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=92.7, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=131.15, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='2', width=175.15):
            with Note(default_x=15.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=54.25, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=92.7, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=131.15, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='3', width=176.77):
            with Note(default_x=15.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=54.72, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.63, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=132.55, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='4', width=190.8):
            with Note(default_x=15.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=65.75, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=105.87, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=145.98, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='5', width=202.9):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=94.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=146.18):
            with Attributes():
                with Clef():
                    Sign('C')
                    Line(4)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=8.26, relative_y=30.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=98.15, default_y=-90.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=121.41, default_y=-95.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=175.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(68.41)
            with Note(default_x=80.65, default_y=-103.41):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=104.81, default_y=-103.41):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=120.47, default_y=-108.41):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.14, default_y=-113.41):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='9', width=58.04):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='10', width=178.92):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='11', width=234.03):
            with Attributes():
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=10.82, relative_y=30.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=19.38, default_y=-93.41):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=54.69, default_y=-98.41):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.52, default_y=-93.41):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.36, default_y=-88.41):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=137.66, default_y=-83.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='12', width=189.76):
            with Note(default_x=19.38, default_y=-113.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=49.28, default_y=-118.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.22, default_y=-113.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.16, default_y=-108.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.11, default_y=-103.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='13', width=260.89):
            with Note(default_x=17.8, default_y=-93.41):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=53.11, default_y=-98.41):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.37, default_y=-93.41):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.63, default_y=-88.41):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=141.7, default_y=-83.41):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=169.96, default_y=-88.41):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.23, default_y=-83.41):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.49, default_y=-78.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=229.27):
            with Note(default_x=26.88, default_y=-73.41):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=130.61, default_y=-73.41):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=154.87, default_y=-78.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.14, default_y=-83.41):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.4, default_y=-88.41):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='15', width=214.92):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=82.58, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=180.54, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='16', width=165.85):
            with Note(default_x=32.06, default_y=-70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=59.48, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=86.89, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=131.45, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='17', width=193.91):
            with Note(default_x=20.15, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.29, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=135.67, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='18', width=224.3):
            with Note(default_x=22.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=50.56, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=78.33, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='19', width=274.76):
            with Note(default_x=24.81, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=217.9, default_y=-70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='20', width=252.28):
            with Note(default_x=22.28, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=53.71, default_y=-70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=85.13, default_y=-70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=235.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=82.58, default_y=-70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=166.9, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=200.64, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=263.46):
            with Note(default_x=26.88, default_y=-70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=72.13, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='23', width=254.96):
            with Note(default_x=15.56, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=80.91, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='24', width=227.05):
            with Note(default_x=32.06, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=182.16, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
        with Measure(number='25', width=164.17):
            with Note(default_x=20.15, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.66, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=74.6, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.55, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=129.06, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='26', width=180.42):
            with Note(default_x=15.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=134.47, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='27', width=255.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=114.95, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=137.48, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=162.78, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=185.32, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=207.85, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=230.39, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='28', width=167.92):
            with Note(default_x=19.38, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=50.87, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='29', width=156.37):
            with Note(default_x=19.38, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.68, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='30', width=151.52):
            with Note(default_x=17.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=108.14, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.76, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=253.15):
            with Note(default_x=26.88, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=138.13, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=170.2, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.32, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.44, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=153.43):
            with Note(default_x=19.38, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=119.05, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='33', width=188.47):
            with Note(default_x=31.7, default_y=-70.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='34', width=217.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=82.58, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='35', width=189.68):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=240.86):
            with Note(default_x=15.8, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=123.32, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=212.38, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='37', width=167.92):
            with Note(default_x=15.8, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=109.45, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=143.15, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='38', width=122.54):
            with Note(default_x=15.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='39', width=58.6):
            with Note(default_x=15.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='40', width=151.64):
            with Note(default_x=21.03, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=117.26, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='41', width=177.46):
            with Note(default_x=15.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=133.75, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='42', width=430.11):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(73.43)
            with Note(default_x=94.62, default_y=-113.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=337.84, default_y=-113.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='43', width=358.24):
            with Attributes():
                with Key():
                    Fifths(2)
            with Note(default_x=38.63, default_y=-133.43):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=37.68)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=37.68)
            with Note(default_x=268.3, default_y=-113.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=312.47, default_y=-103.43):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Dashes(type='stop', number=1)
        with Measure(number='44', width=331.23):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=7.68, relative_y=30.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-98.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=85.54, default_y=-113.43):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=129.13, default_y=-118.43):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=172.71, default_y=-123.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=242.45, default_y=-123.43):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=286.04, default_y=-128.43):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='45', width=206.44):
            with Note(default_x=15.8, default_y=-133.43):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='0', implicit='yes', width=144.26):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='1', width=175.15):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='2', width=175.15):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=176.77):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='4', width=190.8):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='5', width=202.9):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=94.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=146.18):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='8', width=175.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='9', width=58.04):
            with Note(default_x=15.8, default_y=-248.41):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
        with Measure(number='10', width=178.92):
            with Note(default_x=26.88, default_y=-258.41):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=89.78, default_y=-253.41):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
            with Note(default_x=115.08, default_y=-248.41):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
            with Note(default_x=141.48, default_y=-243.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='11', width=234.03):
            with Note(default_x=19.38, default_y=-238.41):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=137.66, default_y=-223.41):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=199.63, default_y=-238.41):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='12', width=189.76):
            with Note(default_x=19.38, default_y=-233.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=106.11, default_y=-223.41):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=155.36, default_y=-233.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='13', width=260.89):
            with Note(default_x=17.8, default_y=-238.41):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=141.7, default_y=-223.41):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.13, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling;')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=226.49, default_y=-248.41):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
        with Measure(number='14', width=229.27):
            with Note(default_x=26.88, default_y=-258.41):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=105.31, default_y=-253.41):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
            with Note(default_x=130.61, default_y=-248.41):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
            with Note(default_x=179.14, default_y=-243.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='15', width=214.92):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=82.58, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=143.42, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note(default_x=180.54, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
        with Measure(number='16', width=165.85):
            with Note(default_x=32.06, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('young')
            with Note(default_x=86.89, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
            with Note(default_x=131.45, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
        with Measure(number='17', width=193.91):
            with Note(default_x=20.15, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.66, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=135.67, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=-19.05, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text("1.'Twas")
                with Lyric(number='2', default_x=-16.16, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.And')
                with Lyric(number='3', default_x=-16.16, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.They')
        with Measure(number='18', width=224.3):
            with Note(default_x=22.8, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('on')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('many')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text("wou'd")
            with Note(default_x=78.33, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=122.75, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mon')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gal')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('bide')
            with Note(default_x=167.17, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('day')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('lant')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
        with Measure(number='19', width=274.76):
            with Note(default_x=24.81, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mor')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Scot')
                with Lyric(number='3', default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('chase')
                    Extend()
            with Note(default_x=107.7, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('tish')
                with Lyric(number='3', default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                    Extend()
            with Note(default_x=162.64, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.89, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('ning,')
                with Lyric(number='2', default_x=9.03, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('chief,')
                with Lyric(number='3', default_x=8.97, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('roes,')
            with Note(default_x=217.9, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('when')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('came')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('or')
        with Measure(number='20', width=252.28):
            with Note(default_x=22.28, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('birds')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('round')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('start')
            with Note(default_x=85.13, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('were')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('their')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
            with Note(default_x=137.55, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sing')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('Prince')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('moun')
            with Note(default_x=187.83, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('tain')
        with Measure(number='21', width=235.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=82.58, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.48, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('clear;')
                with Lyric(number='2', default_x=9.31, default_y=-75.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('cheer;')
                with Lyric(number='3', default_x=9.31, default_y=-100.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('deer;')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=200.64, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('that')
                with Lyric(number='2', default_x=6.58, default_y=-75.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
                with Lyric(number='3', default_x=6.58, default_y=-100.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('but')
        with Measure(number='22', width=263.46):
            with Note(default_x=26.88, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
                with Lyric(number='2', default_x=6.58, default_y=-75.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
                with Lyric(number='3', default_x=6.58, default_y=-100.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('aff')
            with Note(default_x=100.4, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
                with Lyric(number='2', default_x=6.58, default_y=-75.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
                with Lyric(number='3', default_x=6.58, default_y=-100.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('they')
            with Note(default_x=157.73, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
                with Lyric(number='2', default_x=6.58, default_y=-75.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
                with Lyric(number='3', default_x=6.58, default_y=-100.08, relative_y=-30.0):
                    Syllabic('single')
                    Text("march'd")
            with Note(default_x=216.62, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-75.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('their')
                with Lyric(number='3', default_x=8.31, default_y=-100.08, relative_y=-30.0):
                    Syllabic('single')
                    Text("wi'")
        with Measure(number='23', width=254.96):
            with Note(default_x=15.56, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('high')
                with Lyric(number='2', default_y=-75.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
                with Lyric(number='3', default_y=-100.08, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=80.91, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('lands')
            with Note(default_x=133.97, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.34, default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('came,')
                with Lyric(number='2', default_x=8.87, default_y=-75.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
                with Lyric(number='3', default_x=8.88, default_y=-100.08, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie,')
            with Note(default_x=187.03, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                    Extend()
                with Lyric(number='2', default_y=-75.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                    Extend()
                with Lyric(number='3', default_y=-100.08, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                    Extend()
            with Note(default_x=220.19, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='24', width=227.05):
            with Note(default_x=32.06, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gal')
                with Lyric(number='2', default_x=6.58, default_y=-75.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('young')
                with Lyric(number='3', default_x=6.58, default_y=-100.08, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gal')
            with Note(default_x=104.81, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('lant')
                with Lyric(number='3', default_x=6.58, default_y=-100.08, relative_y=-30.0):
                    Syllabic('end')
                    Text('lant')
            with Note(default_x=138.86, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
                with Lyric(number='2', default_x=6.58, default_y=-75.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
                with Lyric(number='3', default_x=6.58, default_y=-100.08, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
            with Note(default_x=182.16, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.69, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
                with Lyric(number='2', default_x=6.58, default_y=-75.88, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
                with Lyric(number='3', default_x=6.58, default_y=-100.08, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
        with Measure(number='25', width=164.17):
            with Note(default_x=20.15, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.66, default_y=-51.69, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
                with Lyric(number='2', default_x=8.66, default_y=-75.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
                with Lyric(number='3', default_x=8.66, default_y=-100.08, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='26', width=180.42):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=134.47, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.69, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
                    Extend()
            with Note(default_x=155.66, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='27', width=255.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=78.9, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=137.48, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
            with Note(default_x=162.78, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
            with Note(default_x=207.85, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='28', width=167.92):
            with Note(default_x=19.38, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=82.35, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=133.52, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='29', width=156.37):
            with Note(default_x=19.38, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=75.99, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=121.97, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='30', width=151.52):
            with Note(default_x=17.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=77.37, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.13, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling;')
            with Note(default_x=108.14, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                    Extend()
            with Note(default_x=126.76, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=253.15):
            with Note(default_x=26.88, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=111.02, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
            with Note(default_x=138.13, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
            with Note(default_x=197.32, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='32', width=153.43):
            with Note(default_x=19.38, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=81.93, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-47.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note(default_x=119.05, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
        with Measure(number='33', width=188.47):
            with Note(default_x=32.06, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('young')
            with Note(default_x=107.29, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
            with Note(default_x=156.2, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.94, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
        with Measure(number='34', width=217.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=82.58, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.66, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='35', width=189.68):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=240.86):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='37', width=167.92):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='38', width=122.54):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='39', width=58.6):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='40', width=151.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='41', width=177.46):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='42', width=430.11):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-153.43)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='43', width=358.24):
            with Attributes():
                with Key():
                    Fifths(2)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='44', width=331.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='45', width=206.44):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='0', implicit='yes', width=144.26):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='1', width=175.15):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='2', width=175.15):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=176.77):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='4', width=190.8):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='5', width=202.9):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=94.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=146.18):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='8', width=175.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.24)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='9', width=58.04):
            with Note(default_x=15.8, default_y=-391.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
        with Measure(number='10', width=178.92):
            with Note(default_x=26.88, default_y=-391.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=89.78, default_y=-396.65):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
            with Note(default_x=115.08, default_y=-391.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
            with Note(default_x=141.48, default_y=-386.65):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='11', width=234.03):
            with Note(default_x=19.38, default_y=-381.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=137.66, default_y=-381.65):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=8.87, default_y=-51.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=199.63, default_y=-381.65):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='12', width=189.76):
            with Note(default_x=19.38, default_y=-376.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=106.11, default_y=-376.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.87, default_y=-51.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=155.36, default_y=-376.65):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='13', width=260.89):
            with Note(default_x=17.8, default_y=-381.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=141.7, default_y=-381.65):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.13, default_y=-51.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling;')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=226.49, default_y=-391.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
        with Measure(number='14', width=229.27):
            with Note(default_x=26.88, default_y=-391.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=105.31, default_y=-396.65):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
            with Note(default_x=130.61, default_y=-391.65):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
            with Note(default_x=179.14, default_y=-386.65):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='15', width=214.92):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(145.22)
            with Note(default_x=82.58, default_y=-430.22):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=143.42, default_y=-430.22):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.87, default_y=-46.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note(default_x=180.54, default_y=-425.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
        with Measure(number='16', width=165.85):
            with Note(default_x=32.06, default_y=-420.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('young')
            with Note(default_x=86.89, default_y=-420.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
            with Note(default_x=131.45, default_y=-420.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
        with Measure(number='17', width=193.91):
            with Note(default_x=20.15, default_y=-440.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.66, default_y=-46.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=135.67, default_y=-430.22):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=-19.05, default_y=-46.12, relative_y=-30.0):
                    Syllabic('single')
                    Text("1.'Twas")
                with Lyric(number='2', default_x=-16.16, default_y=-70.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.And')
                with Lyric(number='3', default_x=-16.16, default_y=-94.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.They')
        with Measure(number='18', width=224.3):
            with Note(default_x=22.8, default_y=-435.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('on')
                with Lyric(number='2', default_x=6.58, default_y=-70.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('many')
                with Lyric(number='3', default_x=6.58, default_y=-94.52, relative_y=-30.0):
                    Syllabic('single')
                    Text("wou'd")
            with Note(default_x=78.33, default_y=-420.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
                with Lyric(number='2', default_x=6.58, default_y=-70.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
                with Lyric(number='3', default_x=6.58, default_y=-94.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=122.75, default_y=-420.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mon')
                with Lyric(number='2', default_x=6.58, default_y=-70.32, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gal')
                with Lyric(number='3', default_x=6.58, default_y=-94.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('bide')
            with Note(default_x=167.17, default_y=-420.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('day')
                with Lyric(number='2', default_x=6.58, default_y=-70.32, relative_y=-30.0):
                    Syllabic('end')
                    Text('lant')
                with Lyric(number='3', default_x=6.58, default_y=-94.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
        with Measure(number='19', width=274.76):
            with Note(default_x=24.81, default_y=-420.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-46.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mor')
                with Lyric(number='2', default_x=6.58, default_y=-70.32, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Scot')
                with Lyric(number='3', default_y=-94.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('chase')
                    Extend()
            with Note(default_x=107.7, default_y=-425.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='2', default_x=6.58, default_y=-70.32, relative_y=-30.0):
                    Syllabic('end')
                    Text('tish')
                with Lyric(number='3', default_y=-94.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                    Extend()
            with Note(default_x=162.64, default_y=-430.22):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.89, default_y=-46.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('ning,')
                with Lyric(number='2', default_x=9.03, default_y=-70.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('chief,')
                with Lyric(number='3', default_x=8.97, default_y=-94.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('roes,')
            with Note(default_x=217.9, default_y=-430.22):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('when')
                with Lyric(number='2', default_x=6.58, default_y=-70.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('came')
                with Lyric(number='3', default_x=6.58, default_y=-94.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('or')
        with Measure(number='20', width=252.28):
            with Note(default_x=22.28, default_y=-435.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('birds')
                with Lyric(number='2', default_x=6.58, default_y=-70.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('round')
                with Lyric(number='3', default_x=6.58, default_y=-94.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('start')
            with Note(default_x=85.13, default_y=-420.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('single')
                    Text('were')
                with Lyric(number='2', default_x=6.58, default_y=-70.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('their')
                with Lyric(number='3', default_x=6.58, default_y=-94.52, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
            with Note(default_x=137.55, default_y=-420.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sing')
                with Lyric(number='2', default_x=6.58, default_y=-70.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('Prince')
                with Lyric(number='3', default_x=6.58, default_y=-94.52, relative_y=-30.0):
                    Syllabic('begin')
                    Text('moun')
            with Note(default_x=187.83, default_y=-420.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.12, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing')
                with Lyric(number='2', default_x=6.58, default_y=-70.32, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
                with Lyric(number='3', default_x=6.58, default_y=-94.52, relative_y=-30.0):
                    Syllabic('end')
                    Text('tain')
        with Measure(number='21', width=235.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(150.74)
            with Note(default_x=82.58, default_y=-425.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=0.52, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('clear;')
                    Extend()
                with Lyric(number='2', default_x=0.52, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('cheer;')
                    Extend()
                with Lyric(number='3', default_x=0.52, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('deer;')
                    Extend()
            with Note(default_x=145.82, default_y=-430.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=166.9, default_y=-435.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=200.64, default_y=-430.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('that')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('but')
        with Measure(number='22', width=263.46):
            with Note(default_x=26.88, default_y=-425.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('aff')
            with Note(default_x=100.4, default_y=-430.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('they')
            with Note(default_x=157.73, default_y=-425.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text("march'd")
            with Note(default_x=216.62, default_y=-420.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('their')
                with Lyric(number='3', default_x=8.31, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text("wi'")
        with Measure(number='23', width=254.96):
            with Note(default_x=15.56, default_y=-425.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('high')
                with Lyric(number='2', default_y=-75.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
                with Lyric(number='3', default_y=-99.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=80.91, default_y=-435.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('lands')
            with Note(default_x=133.97, default_y=-425.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.34, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('came,')
                with Lyric(number='2', default_x=8.87, default_y=-75.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
                with Lyric(number='3', default_x=8.88, default_y=-99.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie,')
            with Note(default_x=187.03, default_y=-440.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                    Extend()
                with Lyric(number='2', default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                    Extend()
                with Lyric(number='3', default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                    Extend()
            with Note(default_x=220.19, default_y=-435.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='24', width=227.05):
            with Note(default_x=32.06, default_y=-430.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gal')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('young')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gal')
            with Note(default_x=104.81, default_y=-440.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('lant')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('lant')
            with Note(default_x=138.86, default_y=-435.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
            with Note(default_x=182.16, default_y=-445.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
        with Measure(number='25', width=164.17):
            with Note(default_x=20.15, default_y=-450.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.66, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
                with Lyric(number='2', default_x=8.66, default_y=-75.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
                with Lyric(number='3', default_x=8.66, default_y=-99.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='26', width=180.42):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=134.47, default_y=-435.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
                    Extend()
            with Note(default_x=155.66, default_y=-440.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='27', width=255.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(95.74)
            with Note(default_x=78.9, default_y=-390.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=137.48, default_y=-395.74):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
            with Note(default_x=162.78, default_y=-390.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
            with Note(default_x=207.85, default_y=-385.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='28', width=167.92):
            with Note(default_x=19.38, default_y=-380.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=82.35, default_y=-380.74):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=8.87, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=133.52, default_y=-380.74):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='29', width=156.37):
            with Note(default_x=19.38, default_y=-375.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=75.99, default_y=-365.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=121.97, default_y=-375.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='30', width=151.52):
            with Note(default_x=17.8, default_y=-380.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=77.37, default_y=-380.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=9.13, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling;')
            with Note(default_x=108.14, default_y=-370.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                    Extend()
            with Note(default_x=126.76, default_y=-380.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=253.15):
            with Note(default_x=26.88, default_y=-390.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=111.02, default_y=-395.74):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
            with Note(default_x=138.13, default_y=-390.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
            with Note(default_x=197.32, default_y=-385.74):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='32', width=153.43):
            with Note(default_x=19.38, default_y=-380.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=81.93, default_y=-365.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note(default_x=119.05, default_y=-375.74):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
        with Measure(number='33', width=188.47):
            with Note(default_x=32.06, default_y=-370.74):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('young')
            with Note(default_x=107.29, default_y=-360.74):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
            with Note(default_x=156.2, default_y=-355.74):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
        with Measure(number='34', width=217.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(75.4)
            with Note(default_x=82.58, default_y=-335.4):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.66, default_y=-40.0, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='35', width=189.68):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=240.86):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='37', width=167.92):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='38', width=122.54):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='39', width=58.6):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='40', width=151.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='41', width=177.46):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='42', width=430.11):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='43', width=358.24):
            with Attributes():
                with Key():
                    Fifths(2)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='44', width=331.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='45', width=206.44):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='0', implicit='yes', width=144.26):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='1', width=175.15):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='2', width=175.15):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=176.77):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='4', width=190.8):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='5', width=202.9):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=94.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=146.18):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='8', width=175.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-386.65)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='9', width=58.04):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='10', width=178.92):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='11', width=234.03):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='12', width=189.76):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='13', width=260.89):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='14', width=229.27):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='15', width=214.92):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-435.22)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='16', width=165.85):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=193.91):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='18', width=224.3):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='19', width=274.76):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='20', width=252.28):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='21', width=235.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-440.74)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='22', width=263.46):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='23', width=254.96):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='24', width=227.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='25', width=164.17):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='26', width=180.42):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=255.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-385.74)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=167.92):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=156.37):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='30', width=151.52):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='31', width=253.15):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=153.43):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='33', width=188.47):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='34', width=217.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-365.4)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='35', width=189.68):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=240.86):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='37', width=167.92):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='38', width=122.54):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='39', width=58.6):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='40', width=151.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='41', width=177.46):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='42', width=430.11):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='43', width=358.24):
            with Attributes():
                with Key():
                    Fifths(2)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='44', width=331.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='45', width=206.44):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='0', implicit='yes', width=144.26):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='1', width=175.15):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='2', width=175.15):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=176.77):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='4', width=190.8):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='5', width=202.9):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=94.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=146.18):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='8', width=175.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(478.18)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='9', width=58.04):
            with Note(default_x=15.8, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
        with Measure(number='10', width=178.92):
            with Note(default_x=26.88, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=89.78, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
            with Note(default_x=115.08, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
            with Note(default_x=141.48, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='11', width=234.03):
            with Note(default_x=19.38, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=137.66, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-51.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=199.63, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='12', width=189.76):
            with Note(default_x=19.38, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=106.11, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-51.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=155.36, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='13', width=260.89):
            with Note(default_x=17.8, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=141.7, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.13, default_y=-51.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling;')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=226.49, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
        with Measure(number='14', width=229.27):
            with Note(default_x=26.88, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=105.31, default_y=-478.18):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
            with Note(default_x=130.61, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
            with Note(default_x=179.14, default_y=-498.18):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='15', width=214.92):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(579.41)
            with Note(default_x=82.58, default_y=-599.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=143.42, default_y=-599.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note(default_x=180.54, default_y=-604.41):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
        with Measure(number='16', width=165.85):
            with Note(default_x=32.06, default_y=-589.41):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('young')
            with Note(default_x=86.89, default_y=-579.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
            with Note(default_x=131.45, default_y=-599.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
        with Measure(number='17', width=193.91):
            with Note(default_x=20.15, default_y=-599.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.66, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=135.67, default_y=-579.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=-19.05, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text("1.'Twas")
                with Lyric(number='2', default_x=-16.16, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.And')
                with Lyric(number='3', default_x=-16.16, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.They')
        with Measure(number='18', width=224.3):
            with Note(default_x=22.8, default_y=-579.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('on')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('many')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text("wou'd")
            with Note(default_x=78.33, default_y=-579.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('na')
            with Note(default_x=122.75, default_y=-579.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mon')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gal')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('bide')
            with Note(default_x=167.17, default_y=-579.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('day')
                    Extend()
                with Lyric(number='2', default_y=-75.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('lant')
                    Extend()
                with Lyric(number='3', default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
                    Extend()
            with Note(default_x=194.93, default_y=-584.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='19', width=274.76):
            with Note(default_x=24.81, default_y=-589.41):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('mor')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Scot')
                with Lyric(number='3', default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('chase')
                    Extend()
            with Note(default_x=107.7, default_y=-594.41):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('end')
                    Text('tish')
                with Lyric(number='3', default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                    Extend()
            with Note(default_x=162.64, default_y=-599.41):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.89, default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('ning,')
                with Lyric(number='2', default_x=9.03, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('chief,')
                with Lyric(number='3', default_x=8.97, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('roes,')
            with Note(default_x=217.9, default_y=-579.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('when')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('came')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('or')
        with Measure(number='20', width=252.28):
            with Note(default_x=22.28, default_y=-579.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('birds')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('round')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('start')
            with Note(default_x=85.13, default_y=-579.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('single')
                    Text('were')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('their')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
            with Note(default_x=137.55, default_y=-579.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.17, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sing')
                with Lyric(number='2', default_x=6.58, default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('Prince')
                with Lyric(number='3', default_x=6.58, default_y=-99.57, relative_y=-30.0):
                    Syllabic('begin')
                    Text('moun')
            with Note(default_x=187.83, default_y=-579.41):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.17, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing')
                    Extend()
                with Lyric(number='2', default_y=-75.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
                    Extend()
                with Lyric(number='3', default_y=-99.57, relative_y=-30.0):
                    Syllabic('end')
                    Text('tain')
                    Extend()
            with Note(default_x=219.26, default_y=-584.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=235.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(595.38)
            with Note(default_x=82.58, default_y=-605.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=0.52, default_y=-48.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('clear;')
                    Extend()
                with Lyric(number='2', default_x=0.52, default_y=-72.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('cheer;')
                    Extend()
                with Lyric(number='3', default_x=0.52, default_y=-96.59, relative_y=-30.0):
                    Syllabic('single')
                    Text('deer;')
                    Extend()
            with Note(default_x=145.82, default_y=-610.38):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=166.9, default_y=-615.38):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=200.64, default_y=-620.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('that')
                with Lyric(number='2', default_x=6.58, default_y=-72.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
                with Lyric(number='3', default_x=6.58, default_y=-96.59, relative_y=-30.0):
                    Syllabic('single')
                    Text('but')
        with Measure(number='22', width=263.46):
            with Note(default_x=26.88, default_y=-605.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
                with Lyric(number='2', default_x=6.58, default_y=-72.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
                with Lyric(number='3', default_x=6.58, default_y=-96.59, relative_y=-30.0):
                    Syllabic('single')
                    Text('aff')
            with Note(default_x=100.4, default_y=-605.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
                with Lyric(number='2', default_x=6.58, default_y=-72.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
                with Lyric(number='3', default_x=6.58, default_y=-96.59, relative_y=-30.0):
                    Syllabic('single')
                    Text('they')
            with Note(default_x=157.73, default_y=-605.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
                with Lyric(number='2', default_x=6.58, default_y=-72.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
                with Lyric(number='3', default_x=6.58, default_y=-96.59, relative_y=-30.0):
                    Syllabic('single')
                    Text("march'd")
            with Note(default_x=216.62, default_y=-605.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-72.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('their')
                with Lyric(number='3', default_x=8.31, default_y=-96.59, relative_y=-30.0):
                    Syllabic('single')
                    Text("wi'")
        with Measure(number='23', width=254.96):
            with Note(default_x=15.56, default_y=-605.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('high')
                with Lyric(number='2', default_y=-72.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
                with Lyric(number='3', default_y=-96.59, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=80.91, default_y=-595.38):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('lands')
            with Note(default_x=133.97, default_y=-585.38):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.34, default_y=-48.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('came,')
                with Lyric(number='2', default_x=8.87, default_y=-72.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
                with Lyric(number='3', default_x=8.88, default_y=-96.59, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie,')
            with Note(default_x=187.03, default_y=-585.38):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='2', default_x=6.58, default_y=-72.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='3', default_x=6.58, default_y=-96.59, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
        with Measure(number='24', width=227.05):
            with Note(default_x=32.06, default_y=-585.38):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gal')
                with Lyric(number='2', default_x=6.58, default_y=-72.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('young')
                with Lyric(number='3', default_x=6.58, default_y=-96.59, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gal')
            with Note(default_x=77.75, default_y=-620.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-48.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('lant')
                with Lyric(number='3', default_x=6.58, default_y=-96.59, relative_y=-30.0):
                    Syllabic('end')
                    Text('lant')
            with Note(default_x=138.86, default_y=-605.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.19, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
                with Lyric(number='2', default_x=6.58, default_y=-72.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
                with Lyric(number='3', default_x=6.58, default_y=-96.59, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
            with Note(default_x=182.16, default_y=-600.38):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-48.19, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
                with Lyric(number='2', default_x=6.58, default_y=-72.39, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
                with Lyric(number='3', default_x=6.58, default_y=-96.59, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
        with Measure(number='25', width=164.17):
            with Note(default_x=20.15, default_y=-620.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.66, default_y=-48.19, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
                with Lyric(number='2', default_x=8.66, default_y=-72.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
                with Lyric(number='3', default_x=8.66, default_y=-96.59, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='26', width=180.42):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=134.47, default_y=-605.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-48.19, relative_y=-30.0):
                    Syllabic('single')
                    Text('O')
                    Extend()
            with Note(default_x=155.66, default_y=-610.38):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='27', width=255.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(484.71)
            with Note(default_x=78.9, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=137.48, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
            with Note(default_x=162.78, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
            with Note(default_x=207.85, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='28', width=167.92):
            with Note(default_x=19.38, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=82.35, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-51.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=133.52, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='29', width=156.37):
            with Note(default_x=19.38, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=75.99, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-51.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=121.97, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='30', width=151.52):
            with Note(default_x=17.8, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=77.37, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=9.13, default_y=-51.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling;')
            with Note(default_x=108.14, default_y=-484.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                    Extend()
            with Note(default_x=126.76, default_y=-494.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=253.15):
            with Note(default_x=26.88, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Char')
            with Note(default_x=111.02, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('lie')
            with Note(default_x=138.13, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('is')
            with Note(default_x=197.32, default_y=-509.71):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='32', width=153.43):
            with Note(default_x=19.38, default_y=-494.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dar')
            with Note(default_x=81.93, default_y=-494.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.87, default_y=-51.72, relative_y=-30.0):
                    Syllabic('end')
                    Text('ling,')
            with Note(default_x=119.05, default_y=-494.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
        with Measure(number='33', width=188.47):
            with Note(default_x=32.06, default_y=-494.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('single')
                    Text('young')
            with Note(default_x=107.29, default_y=-484.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('begin')
                    Text('che')
            with Note(default_x=156.2, default_y=-504.71):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.72, relative_y=-30.0):
                    Syllabic('middle')
                    Text('va')
        with Measure(number='34', width=217.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(440.8)
            with Note(default_x=82.58, default_y=-460.8):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=8.66, default_y=-47.42, relative_y=-30.0):
                    Syllabic('end')
                    Text('lier.')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='35', width=189.68):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=240.86):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='37', width=167.92):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='38', width=122.54):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='39', width=58.6):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='40', width=151.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='41', width=177.46):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='42', width=430.11):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='43', width=358.24):
            with Attributes():
                with Key():
                    Fifths(2)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='44', width=331.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='45', width=206.44):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P7'):
        with Measure(number='0', implicit='yes', width=144.26):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(210.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('2')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=99.95, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=99.95, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=119.5, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='1', width=175.15):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=54.25, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=92.7, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=131.15, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.03, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.25, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.48, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=92.7, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=111.93, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.15, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.38, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='2', width=175.15):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=54.25, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=54.25, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=92.7, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=92.7, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=131.15, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.15, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.03, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.25, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.48, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=92.7, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=111.93, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.15, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.38, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=176.77):
            with Note(default_x=15.8, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-175.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=54.72, default_y=-205.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=54.72, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=93.63, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=93.63, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=132.55, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=132.55, default_y=-190.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.26, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.72, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.17, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.63, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.09, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.55, default_y=-350.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.0, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=190.8):
            with Note(default_x=15.8, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=65.75, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=65.75, default_y=-200.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=105.87, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=105.87, default_y=-200.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=145.98, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=145.98, default_y=-200.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.86, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.75, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.81, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=105.87, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.92, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.98, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.03, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='5', width=202.9):
            with Note(default_x=15.8, default_y=-210.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-200.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=58.11, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=79.26, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=100.42, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=151.47, default_y=-200.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.95, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.11, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.26, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=100.42, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.57, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.47, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.13, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='6', width=94.64):
            with Note(default_x=15.8, default_y=-195.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=50.9, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-310.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=50.9, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=50.9, default_y=-305.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='7', width=146.18):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=39.16, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=55.54, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.93, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=98.15, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=39.16, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=55.54, default_y=-320.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.93, default_y=-325.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=98.15, default_y=-330.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='8', width=175.12):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(121.79)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.65, default_y=-684.98):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=104.81, default_y=-664.98):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=120.47, default_y=-669.98):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.14, default_y=-674.98):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=80.65, default_y=-764.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=104.81, default_y=-744.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=120.47, default_y=-749.98):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.14, default_y=-754.98):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='9', width=58.04):
            with Note(default_x=15.8, default_y=-674.98):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-649.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-639.98):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=15.8, default_y=-799.98):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-764.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='10', width=178.92):
            with Note(default_x=26.88, default_y=-674.98):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=26.88, default_y=-649.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=115.08, default_y=-649.98):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=115.08, default_y=-639.98):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=141.48, default_y=-644.98):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=141.48, default_y=-634.98):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=26.88, default_y=-799.98):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=26.88, default_y=-764.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=115.08, default_y=-799.98):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=115.08, default_y=-764.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='11', width=234.03):
            with Note(default_x=19.38, default_y=-639.98):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=19.38, default_y=-629.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=137.66, default_y=-639.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=137.66, default_y=-614.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=199.63, default_y=-639.98):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=199.63, default_y=-629.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=19.38, default_y=-799.98):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=19.38, default_y=-764.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=137.66, default_y=-764.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=137.66, default_y=-729.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=199.63, default_y=-764.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=199.63, default_y=-729.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=189.76):
            with Note(default_x=19.38, default_y=-634.98):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=19.38, default_y=-624.98):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=106.11, default_y=-634.98):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=106.11, default_y=-624.98):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=106.11, default_y=-614.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=155.36, default_y=-634.98):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=155.36, default_y=-624.98):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=19.38, default_y=-764.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=19.38, default_y=-729.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=106.11, default_y=-764.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=106.11, default_y=-729.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=155.36, default_y=-764.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.36, default_y=-729.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=260.89):
            with Note(default_x=17.8, default_y=-639.98):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=17.8, default_y=-629.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=141.7, default_y=-639.98):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=141.7, default_y=-614.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=226.49, default_y=-649.98):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=226.49, default_y=-639.98):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=17.8, default_y=-764.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=17.8, default_y=-729.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=141.7, default_y=-764.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=141.7, default_y=-729.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=226.49, default_y=-764.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=229.27):
            with Note(default_x=26.88, default_y=-649.98):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=105.31, default_y=-654.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=105.31, default_y=-644.98):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=130.61, default_y=-649.98):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=130.61, default_y=-639.98):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=179.14, default_y=-644.98):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=179.14, default_y=-634.98):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=26.88, default_y=-764.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=105.31, default_y=-779.98):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=105.31, default_y=-744.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=130.61, default_y=-764.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=130.61, default_y=-729.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=179.14, default_y=-764.98):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=179.14, default_y=-729.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=214.92):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(178.09)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=82.58, default_y=-797.5):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=82.58, default_y=-787.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=143.42, default_y=-797.5):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=143.42, default_y=-772.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=180.54, default_y=-792.5):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=180.54, default_y=-767.5):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=82.58, default_y=-922.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=82.58, default_y=-887.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=143.42, default_y=-922.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=143.42, default_y=-887.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=180.54, default_y=-927.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=180.54, default_y=-892.5):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=165.85):
            with Note(default_x=32.06, default_y=-787.5):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=32.06, default_y=-762.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=86.89, default_y=-802.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=86.89, default_y=-787.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=86.89, default_y=-777.5):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=86.89, default_y=-767.5):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=131.45, default_y=-807.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=131.45, default_y=-772.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=32.06, default_y=-912.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=32.06, default_y=-877.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=86.89, default_y=-902.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=86.89, default_y=-867.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=131.45, default_y=-922.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=131.45, default_y=-887.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=193.91):
            with Note(default_x=20.15, default_y=-807.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=20.15, default_y=-772.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=55.29, default_y=-797.5):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=90.44, default_y=-802.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=113.7, default_y=-807.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=135.67, default_y=-807.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=135.67, default_y=-797.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=135.67, default_y=-772.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=20.15, default_y=-922.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=20.15, default_y=-887.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=55.29, default_y=-877.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=90.44, default_y=-882.5):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=113.7, default_y=-887.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=135.67, default_y=-902.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='18', width=224.3):
            with Note(default_x=22.8, default_y=-812.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=22.8, default_y=-802.5):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=22.8, default_y=-777.5):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=78.33, default_y=-812.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=78.33, default_y=-787.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=122.75, default_y=-807.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=122.75, default_y=-782.5):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=167.17, default_y=-802.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=167.17, default_y=-777.5):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=22.8, default_y=-902.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=78.33, default_y=-902.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=122.75, default_y=-902.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=167.17, default_y=-902.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=194.93, default_y=-907.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=274.76):
            with Note(default_x=24.81, default_y=-807.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=24.81, default_y=-787.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=24.81, default_y=-772.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=162.64, default_y=-787.5):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=162.64, default_y=-762.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=217.9, default_y=-807.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=217.9, default_y=-797.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=217.9, default_y=-772.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=24.81, default_y=-912.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=52.44, default_y=-907.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.07, default_y=-912.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.7, default_y=-917.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=162.64, default_y=-922.5):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=190.27, default_y=-917.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.9, default_y=-912.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.53, default_y=-907.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='20', width=252.28):
            with Note(default_x=22.28, default_y=-812.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=22.28, default_y=-802.5):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=22.28, default_y=-777.5):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=85.13, default_y=-812.5):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=85.13, default_y=-787.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=137.55, default_y=-807.5):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.55, default_y=-782.5):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=187.83, default_y=-802.5):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=187.83, default_y=-777.5):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=22.28, default_y=-902.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=85.13, default_y=-902.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=137.55, default_y=-902.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=187.83, default_y=-902.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=219.26, default_y=-907.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=235.97):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(172.01)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=82.58, default_y=-817.39):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=82.58, default_y=-797.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=82.58, default_y=-782.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=166.9, default_y=-817.39):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=166.9, default_y=-807.39):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=166.9, default_y=-782.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=200.64, default_y=-812.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=200.64, default_y=-802.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=200.64, default_y=-777.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=82.58, default_y=-922.39):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=103.66, default_y=-917.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.74, default_y=-922.39):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.82, default_y=-927.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=166.9, default_y=-932.39):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=200.64, default_y=-937.39):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='22', width=263.46):
            with Note(default_x=26.88, default_y=-807.39):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=26.88, default_y=-797.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=26.88, default_y=-772.39):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=157.73, default_y=-807.39):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=157.73, default_y=-797.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=157.73, default_y=-772.39):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=216.62, default_y=-792.39):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=216.62, default_y=-782.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=26.88, default_y=-922.39):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=157.73, default_y=-922.39):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='23', width=254.96):
            with Note(default_x=15.56, default_y=-797.39):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.56, default_y=-787.39):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=80.91, default_y=-807.39):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=80.91, default_y=-797.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=133.97, default_y=-832.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=133.97, default_y=-807.39):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=187.03, default_y=-812.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=187.03, default_y=-802.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=220.19, default_y=-807.39):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.19, default_y=-797.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.56, default_y=-922.39):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=133.97, default_y=-937.39):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=133.97, default_y=-902.39):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='24', width=227.05):
            with Note(default_x=32.06, default_y=-802.39):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=32.06, default_y=-792.39):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=104.81, default_y=-812.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=104.81, default_y=-802.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=138.86, default_y=-807.39):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=138.86, default_y=-797.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=182.16, default_y=-827.39):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=182.16, default_y=-817.39):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=182.16, default_y=-807.39):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=32.06, default_y=-937.39):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=32.06, default_y=-902.39):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=138.86, default_y=-922.39):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=182.16, default_y=-917.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='25', width=164.17):
            with Note(default_x=20.15, default_y=-837.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=20.15, default_y=-822.39):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=20.15, default_y=-812.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=53.66, default_y=-827.39):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=74.6, default_y=-837.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=95.55, default_y=-832.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=129.06, default_y=-852.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=129.06, default_y=-842.39):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=20.15, default_y=-937.39):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=20.15, default_y=-902.39):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=53.66, default_y=-927.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=53.66, default_y=-902.39):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=95.55, default_y=-922.39):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=95.55, default_y=-902.39):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=129.06, default_y=-917.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=129.06, default_y=-907.39):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=180.42):
            with Note(default_x=15.8, default_y=-847.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=49.71, default_y=-827.39):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=70.9, default_y=-837.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=92.09, default_y=-832.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=113.28, default_y=-837.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=134.47, default_y=-842.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=155.66, default_y=-847.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-937.39):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-902.39):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=49.71, default_y=-907.39):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=70.9, default_y=-917.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=92.09, default_y=-912.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=113.28, default_y=-917.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=134.47, default_y=-922.39):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=155.66, default_y=-927.39):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='27', width=255.15):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(131.79)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=78.9, default_y=-701.51):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=162.78, default_y=-666.51):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=162.78, default_y=-656.51):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=207.85, default_y=-661.51):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=207.85, default_y=-651.51):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=78.9, default_y=-781.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=162.78, default_y=-781.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=162.78, default_y=-746.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='28', width=167.92):
            with Note(default_x=19.38, default_y=-656.51):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=19.38, default_y=-646.51):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=82.35, default_y=-656.51):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=82.35, default_y=-631.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=133.52, default_y=-656.51):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=133.52, default_y=-646.51):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=19.38, default_y=-781.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=19.38, default_y=-746.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=82.35, default_y=-781.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=82.35, default_y=-746.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='29', width=156.37):
            with Note(default_x=19.38, default_y=-651.51):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=19.38, default_y=-641.51):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=75.99, default_y=-651.51):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=75.99, default_y=-641.51):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=75.99, default_y=-631.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=121.97, default_y=-651.51):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=121.97, default_y=-641.51):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=19.38, default_y=-781.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=19.38, default_y=-746.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=75.99, default_y=-781.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=75.99, default_y=-746.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='30', width=151.52):
            with Note(default_x=17.8, default_y=-656.51):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=17.8, default_y=-646.51):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=77.37, default_y=-656.51):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=77.37, default_y=-646.51):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=77.37, default_y=-631.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=108.14, default_y=-646.51):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.76, default_y=-656.51):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(8.0)
            with Note(default_x=17.8, default_y=-781.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=17.8, default_y=-746.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=77.37, default_y=-781.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=77.37, default_y=-746.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=108.14, default_y=-761.51):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.76, default_y=-771.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=253.15):
            with Note(default_x=26.88, default_y=-656.51):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=138.13, default_y=-666.51):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=138.13, default_y=-656.51):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=197.32, default_y=-661.51):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=197.32, default_y=-651.51):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=26.88, default_y=-781.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=138.13, default_y=-781.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=138.13, default_y=-771.51):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=197.32, default_y=-786.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=197.32, default_y=-766.51):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='32', width=153.43):
            with Note(default_x=19.38, default_y=-656.51):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=19.38, default_y=-641.51):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=81.93, default_y=-641.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=81.93, default_y=-631.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=119.05, default_y=-651.51):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=119.05, default_y=-626.51):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=19.38, default_y=-771.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=19.38, default_y=-761.51):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=81.93, default_y=-771.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=81.93, default_y=-756.51):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=81.93, default_y=-746.51):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=107.19, default_y=-771.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=119.05, default_y=-766.51):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=119.05, default_y=-756.51):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='33', width=188.47):
            with Note(default_x=32.06, default_y=-646.51):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=32.06, default_y=-621.51):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=107.29, default_y=-661.51):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=107.29, default_y=-646.51):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=107.29, default_y=-636.51):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=107.29, default_y=-626.51):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=32.06, default_y=-771.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=50.87, default_y=-776.51):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.68, default_y=-771.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.48, default_y=-766.51):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.29, default_y=-796.51):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=107.29, default_y=-761.51):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='34', width=217.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(112.84)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=82.58, default_y=-603.64):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=82.58, default_y=-568.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=112.47, default_y=-608.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.14, default_y=-603.64):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.81, default_y=-598.64):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=169.69, default_y=-603.64):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=169.69, default_y=-593.64):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=192.57, default_y=-598.64):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=192.57, default_y=-588.64):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=82.58, default_y=-718.64):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=82.58, default_y=-683.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=169.69, default_y=-743.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=169.69, default_y=-733.64):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=192.57, default_y=-748.64):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=192.57, default_y=-728.64):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='35', width=189.68):
            with Note(default_x=15.8, default_y=-593.64):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=15.8, default_y=-583.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=39.07, default_y=-578.64):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.33, default_y=-573.64):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.64, default_y=-573.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.9, default_y=-568.64):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=154.49, default_y=-563.64):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-733.64):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=15.8, default_y=-723.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=120.9, default_y=-733.64):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=120.9, default_y=-718.64):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=120.9, default_y=-708.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=154.49, default_y=-728.64):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=154.49, default_y=-718.64):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='36', width=240.86):
            with Note(default_x=15.8, default_y=-558.64):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.68, default_y=-568.64):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.56, default_y=-583.64):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=96.44, default_y=-558.64):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=123.32, default_y=-563.64):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=158.62, default_y=-573.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.5, default_y=-583.64):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.38, default_y=-568.64):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-723.64):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=123.32, default_y=-723.64):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=212.38, default_y=-743.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=212.38, default_y=-708.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='37', width=167.92):
            with Note(default_x=15.8, default_y=-568.64):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=44.06, default_y=-583.64):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=63.53, default_y=-588.64):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=81.19, default_y=-593.64):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.45, default_y=-593.64):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=143.15, default_y=-598.64):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-743.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-708.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=44.06, default_y=-723.64):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=63.53, default_y=-728.64):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=81.19, default_y=-733.64):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.45, default_y=-733.64):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=143.15, default_y=-738.64):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='38', width=122.54):
            with Note(default_x=15.8, default_y=-603.64):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=41.54, default_y=-583.64):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=61.0, default_y=-588.64):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=77.09, default_y=-593.64):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=93.18, default_y=-598.64):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-743.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=41.54, default_y=-723.64):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=61.0, default_y=-728.64):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=77.09, default_y=-733.64):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=93.18, default_y=-738.64):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='39', width=58.6):
            with Note(default_x=15.8, default_y=-603.64):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-568.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=15.8, default_y=-733.64):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=33.83, default_y=-728.64):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='40', width=151.64):
            with Note(default_x=21.03, default_y=-608.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=21.03, default_y=-573.64):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=53.11, default_y=-608.64):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=53.11, default_y=-583.64):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=85.19, default_y=-603.64):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=85.19, default_y=-578.64):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=117.26, default_y=-598.64):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=117.26, default_y=-573.64):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=21.03, default_y=-723.64):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=53.11, default_y=-723.64):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=85.19, default_y=-723.64):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=117.26, default_y=-723.64):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='41', width=177.46):
            with Note(default_x=15.8, default_y=-593.64):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-568.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=72.61, default_y=-588.64):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=72.61, default_y=-563.64):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=95.88, default_y=-583.64):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.88, default_y=-558.64):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=133.75, default_y=-583.64):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=133.75, default_y=-568.64):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=15.8, default_y=-723.64):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.74, default_y=-728.64):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.67, default_y=-733.64):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.61, default_y=-738.64):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=95.88, default_y=-743.64):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=114.81, default_y=-738.64):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.75, default_y=-733.64):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.69, default_y=-728.64):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='42', width=430.11):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(235.13)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=94.62, default_y=-240.13):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=94.62, default_y=-225.13):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=94.62, default_y=-215.13):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=175.69, default_y=-250.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=175.69, default_y=-225.13):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=256.77, default_y=-245.13):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=256.77, default_y=-220.13):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=337.84, default_y=-240.13):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=337.84, default_y=-215.13):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=94.62, default_y=-400.13):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=94.62, default_y=-365.13):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=175.69, default_y=-400.13):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=175.69, default_y=-365.13):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=256.77, default_y=-400.13):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=256.77, default_y=-365.13):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=337.84, default_y=-400.13):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=337.84, default_y=-365.13):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='43', width=358.24):
            with Attributes():
                with Key():
                    Fifths(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=38.63, default_y=-235.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=38.63, default_y=-210.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=57.68)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=57.68)
                Staff(1)
            with Note(default_x=109.3, default_y=-225.13):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=109.3, default_y=-210.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=109.3, default_y=-200.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=197.63, default_y=-220.13):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=197.63, default_y=-210.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=197.63, default_y=-195.13):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=268.3, default_y=-225.13):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=268.3, default_y=-215.13):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=268.3, default_y=-195.13):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=38.63, default_y=-360.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.63, default_y=-325.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=109.3, default_y=-360.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=109.3, default_y=-325.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=197.63, default_y=-360.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=197.63, default_y=-325.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=268.3, default_y=-360.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=268.3, default_y=-325.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='44', width=331.23):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=27.68, relative_y=30.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-225.13):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-210.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-200.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=85.54, default_y=-225.13):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=85.54, default_y=-210.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=85.54, default_y=-200.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=172.71, default_y=-225.13):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=172.71, default_y=-210.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=172.71, default_y=-200.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=242.45, default_y=-225.13):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=242.45, default_y=-210.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=242.45, default_y=-200.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-113.38)
                Staff(2)
            with Note(default_x=15.8, default_y=-360.13):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-325.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=85.54, default_y=-395.13):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=85.54, default_y=-360.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=172.71, default_y=-395.13):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=172.71, default_y=-360.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=242.45, default_y=-395.13):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=242.45, default_y=-360.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='45', width=206.44):
            with Note(default_x=15.8, default_y=-225.13):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=34.42, relative_y=10.0)
            with Note(default_x=15.8, default_y=-210.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-200.13):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-395.13):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=5.9, relative_y=10.0)
            with Note(default_x=15.8, default_y=-360.13):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')