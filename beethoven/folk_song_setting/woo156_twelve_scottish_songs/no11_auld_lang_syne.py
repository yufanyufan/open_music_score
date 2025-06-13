with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Auld lang syne')
    with Identification():
        Creator('Arr: Ludwig van Beethoven', type='composer')
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
            PageHeight(1898.54)
            PageWidth(1343.09)
            with PageMargins(type='even'):
                LeftMargin(63.9387)
                RightMargin(63.9387)
                TopMargin(63.9387)
                BottomMargin(127.877)
            with PageMargins(type='odd'):
                LeftMargin(63.9387)
                RightMargin(63.9387)
                TopMargin(63.9387)
                BottomMargin(127.877)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Auld lang syne', default_x=671.547, default_y=1834.6, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Arr: Ludwig van Beethoven', default_x=1279.16, default_y=1705.26, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Fiolin')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Fiolin')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(2)
                MidiProgram(41)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Cello')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Cello')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(7)
                MidiProgram(43)
                Volume(78.7402)
                Pan(0.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P3'):
            PartName('S/A')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('T')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('B')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P6'):
            PartName('Piano', print_object='no')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(11)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=136.89):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(70.1)
                        RightMargin(-0.0)
                    TopSystemDistance(199.34)
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
                    Words('Allegretto', default_x=-36.12, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=60.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='1', width=139.4):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-41.56, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=12.66, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.66, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=78.91, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=78.91, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=108.36, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=108.36, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='2', width=142.42):
            with Note(default_x=12.66, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.66, default_y=-14.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
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
            with Note(default_x=80.51, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=80.51, default_y=-14.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=110.66, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=110.66, default_y=-7.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='3', width=142.42):
            with Note(default_x=12.66, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.66, default_y=-10.5):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=80.51, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.66, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=110.66, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='4', width=143.05):
            with Note(default_x=12.66, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=12.66, default_y=-21.0):
                Chord()
                with Pitch():
                    Step('G')
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
            with Note(default_x=80.84, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=80.84, default_y=-21.0):
                Chord()
                with Pitch():
                    Step('G')
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
        with Measure(number='5', width=123.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=123.7):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=64.6, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=64.6, default_y=-21.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=98.94, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=98.94, default_y=-21.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
        with Measure(number='7', width=193.54):
            with Note(default_x=12.66, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-21.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=66.79, default_y=-45.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=66.79, default_y=-28.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=87.61, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=87.61, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=120.93, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='8', width=319.42):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=112.22, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=112.22, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=180.86, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=180.86, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=222.16, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=222.16, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=275.58, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=275.58, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='9', width=218.29):
            with Note(default_x=23.27, default_y=-38.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=23.27, default_y=-21.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=79.78, default_y=-38.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=79.78, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=124.87, default_y=-38.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=124.87, default_y=-21.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=181.39, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=181.39, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
        with Measure(number='10', width=230.33):
            with Note(default_x=26.65, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=26.65, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=70.14, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=70.14, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=137.17, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=137.17, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=187.48, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=187.48, default_y=-10.5):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='11', width=185.56):
            with Note(default_x=26.01, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=26.01, default_y=-7.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=124.52, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=124.52, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='12', width=240.76):
            with Note(default_x=23.94, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=23.94, default_y=-10.5):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=93.09, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=93.09, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=143.19, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=143.19, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=196.61, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=196.61, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='13', width=317.72):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.4, default_y=-38.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=80.4, default_y=-21.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=150.65, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=150.65, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=213.07, default_y=-38.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=213.07, default_y=-21.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=283.32, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=283.32, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
        with Measure(number='14', width=209.65):
            with Note(default_x=22.36, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=22.36, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=87.75, default_y=-31.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=117.08, default_y=-31.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=167.81, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='15', width=143.75):
            with Note(default_x=22.28, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=22.28, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='16', width=181.23):
            with Note(default_x=12.66, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.66, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=33.2, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.75, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.29, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=94.83, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=115.37, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.92, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.46, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='17', width=175.01):
            with Note(default_x=10.94, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.89, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=50.84, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.78, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=90.73, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=110.68, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=140.63, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=140.63, default_y=-7.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='18', width=167.02):
            with Note(default_x=21.69, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=21.69, default_y=-10.5):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=47.56, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=94.91, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=94.91, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=142.25, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=142.25, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
        with Measure(number='19', width=252.48):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.4, default_y=-21.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=131.82, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=166.66, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=166.66, default_y=-21.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=218.08, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=218.08, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
        with Measure(number='20', width=155.72):
            with Note(default_x=21.69, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=47.56, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=89.26, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=89.26, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=130.95, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=130.95, default_y=-10.5):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Backup():
                Duration(8.0)
            with Note(default_x=21.69, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(4.0)
        with Measure(number='21', width=165.19):
            with Note(default_x=22.53, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=22.53, default_y=-7.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=126.49, default_y=-7.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=126.49, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
        with Measure(number='22', width=147.57):
            with Note(default_x=16.95, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=16.95, default_y=-10.5):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=49.03, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=49.03, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=81.11, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=81.11, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=113.19, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=113.19, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='23', width=198.62):
            with Note(default_x=23.04, default_y=-38.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=23.04, default_y=-21.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=76.59, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=76.59, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=110.67, default_y=-38.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=110.67, default_y=-21.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=164.22, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=164.22, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
        with Measure(number='24', width=146.69):
            with Note(default_x=12.66, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=12.66, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=38.54, default_y=-38.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=38.54, default_y=-31.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=80.23, default_y=-38.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=80.23, default_y=-31.5):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=121.93, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='25', width=128.1):
            with Note(default_x=22.53, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=22.53, default_y=-24.5):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=87.67, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='26', width=224.49):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=80.4, default_y=-42.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=118.89, default_y=-45.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=180.48, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='27', width=148.29):
            with Note(default_x=12.66, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.27, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=105.64, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='28', width=152.14):
            with Note(default_x=12.66, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=38.06, default_y=-10.5):
                with Pitch():
                    Step('C')
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
        with Measure(number='29', width=195.03):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=52.92)
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
            with Note(default_x=132.88, default_y=-35.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='30', width=115.62):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=52.92)
            with Direction(placement='above'):
                with DirectionType():
                    Words('pizz.', relative_y=20.0)
            with Note(default_x=12.66, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
            with Note(default_x=44.6, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=44.6, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=61.63, default_y=-10.5):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=61.63, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=87.83, default_y=7.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='31', width=130.57):
            with Note(default_x=12.66, default_y=3.5):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=46.57, default_y=3.5):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=63.95, default_y=3.5):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=91.76, default_y=10.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=115.62):
            with Note(default_x=12.66, default_y=7.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=44.6, default_y=3.5):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=61.63, default_y=7.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-54.4, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=87.83, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=87.83, default_y=-7.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='33', width=112.61):
            with Direction(placement='above'):
                with DirectionType():
                    Words('arco', relative_y=20.0)
            with Note(default_x=12.66, default_y=-38.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.66, default_y=-28.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.84, default_y=-38.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.84, default_y=-28.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='34', width=332.34):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=80.4, default_y=-28.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=80.4, default_y=-14.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=205.57, default_y=-28.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=205.57, default_y=-14.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='35', width=260.48):
            with Note(default_x=12.66, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.66, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=135.77, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=135.77, default_y=-17.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='36', width=229.03):
            with Note(default_x=12.66, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=12.66, default_y=-3.5):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=131.98, default_y=-14.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=131.98, default_y=-3.5):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=179.7, default_y=-17.5):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=179.7, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='37', width=232.43):
            with Note(default_x=12.66, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=106.82, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=106.82, default_y=-7.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=138.21, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=138.21, default_y=-7.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=199.45, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=199.45, default_y=-10.5):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='38', width=140.09):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=12.66, default_y=-24.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=9.65, relative_y=10.0)
            with Note(default_x=12.66, default_y=-10.5):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='0', implicit='yes', width=136.89):
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
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='1', width=139.4):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=12.66, default_y=-124.5):
                with Pitch():
                    Step('F')
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
            with Note(default_x=78.91, default_y=-124.5):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=108.36, default_y=-124.5):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='2', width=142.42):
            with Note(default_x=12.66, default_y=-107.0):
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
            with Note(default_x=80.51, default_y=-107.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=110.66, default_y=-114.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='3', width=142.42):
            with Note(default_x=12.66, default_y=-117.5):
                with Pitch():
                    Step('A')
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
            with Note(default_x=80.51, default_y=-117.5):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=110.66, default_y=-124.5):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='4', width=143.05):
            with Note(default_x=12.66, default_y=-110.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=80.84, default_y=-110.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='5', width=123.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=123.7):
            with Note(default_x=12.66, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=47.0, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=47.0, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='7', width=193.54):
            with Note(default_x=12.66, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
            with Note(default_x=66.79, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=66.79, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=87.61, default_y=-124.5):
                with Pitch():
                    Step('F')
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
        with Measure(number='8', width=319.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='above'):
                with DirectionType():
                    Words('pizz.', default_y=3.71, relative_y=20.0)
            with Note(default_x=112.22, default_y=-124.5):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=154.46, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=222.16, default_y=-124.5):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=275.58, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='9', width=218.29):
            with Note(default_x=23.27, default_y=-110.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.05, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=124.87, default_y=-110.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=159.65, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='10', width=230.33):
            with Note(default_x=26.65, default_y=-124.5):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=95.92, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=137.17, default_y=-124.5):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=187.48, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='11', width=185.56):
            with Note(default_x=26.01, default_y=-114.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.85, default_y=-89.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=91.68, default_y=-114.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=124.52, default_y=-89.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='12', width=240.76):
            with Note(default_x=23.94, default_y=-110.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.5, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=143.19, default_y=-110.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=196.61, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=317.72):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.4, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=123.63, default_y=-110.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=213.07, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=256.3, default_y=-110.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='14', width=209.65):
            with Note(default_x=22.36, default_y=-124.5):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=62.6, default_y=-89.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=117.08, default_y=-114.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=167.81, default_y=-75.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=143.75):
            with Note(default_x=22.53, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.11, default_y=-75.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=71.69, default_y=-100.0):
                with Pitch():
                    Step('F')
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
        with Measure(number='16', width=181.23):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('arco', relative_y=20.0)
            with Note(default_x=33.2, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=53.75, default_y=-96.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.29, default_y=-93.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=94.83, default_y=-89.5):
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
            with Note(default_x=115.37, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.92, default_y=-93.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.46, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='17', width=175.01):
            with Note(default_x=10.94, default_y=-89.5):
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
            with Note(default_x=30.89, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=50.84, default_y=-93.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.78, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=90.73, default_y=-89.5):
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
            with Note(default_x=110.68, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=140.63, default_y=-89.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='18', width=167.02):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('pizz.', relative_y=20.0)
            with Note(default_x=65.77, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=94.91, default_y=-124.5):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=124.04, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='19', width=252.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.4, default_y=-103.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.04, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=166.66, default_y=-103.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=198.3, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='20', width=155.72):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=63.6, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=89.26, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=114.92, default_y=-75.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='21', width=165.19):
            with Note(default_x=22.53, default_y=-114.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.96, default_y=-89.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=75.38, default_y=-114.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.45, default_y=-89.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='22', width=147.57):
            with Note(default_x=16.95, default_y=-110.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=49.03, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=81.11, default_y=-110.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=113.19, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='23', width=198.62):
            with Note(default_x=23.04, default_y=-110.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.99, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=110.67, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=143.62, default_y=-110.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='24', width=146.69):
            with Note(default_x=12.66, default_y=-131.5):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.57, default_y=-114.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=80.23, default_y=-89.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=105.89, default_y=-75.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='25', width=128.1):
            with Note(default_x=22.53, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=44.25, default_y=-75.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=65.96, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('arco', relative_y=20.0)
            with Note(default_x=87.67, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='26', width=224.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.4, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=180.48, default_y=-103.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='27', width=148.29):
            with Note(default_x=12.66, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.27, default_y=-103.5):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=77.03, default_y=-93.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=105.64, default_y=-96.5):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=152.14):
            with Note(default_x=12.66, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=38.06, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='29', width=195.03):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=52.92)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='30', width=115.62):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=52.92)
            with Direction(placement='above'):
                with DirectionType():
                    Words('pizz.', default_y=19.93, relative_y=20.0)
            with Note(default_x=12.66, default_y=-75.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=44.6, default_y=-75.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=61.63, default_y=-75.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=87.83, default_y=-82.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='31', width=130.57):
            with Note(default_x=12.66, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=46.57, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=63.95, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=91.76, default_y=-86.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=115.62):
            with Note(default_x=12.66, default_y=-82.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=44.6, default_y=-82.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=61.63, default_y=-75.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Sound(dynamics=124.44)
            with Note(default_x=87.83, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='33', width=112.61):
            with Direction(placement='above'):
                with DirectionType():
                    Words('arco', relative_y=20.0)
            with Note(default_x=12.66, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.66, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.84, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.84, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='34', width=332.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.4, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=80.4, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=205.57, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=205.57, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='35', width=260.48):
            with Note(default_x=12.66, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.66, default_y=-117.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=135.77, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=135.77, default_y=-117.5):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='36', width=229.03):
            with Note(default_x=12.66, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=12.66, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=131.98, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=131.98, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=179.7, default_y=-124.5):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='37', width=232.43):
            with Note(default_x=12.66, default_y=-131.5):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=106.82, default_y=-89.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=138.21, default_y=-89.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=199.45, default_y=-93.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='38', width=140.09):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=12.66, default_y=-100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', default_y=1.33, relative_y=10.0)
            with Note(default_x=12.66, default_y=-93.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='0', implicit='yes', width=136.89):
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
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='1', width=139.4):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='2', width=142.42):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=142.42):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='4', width=143.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='5', width=123.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=123.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=193.54):
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
            with Note(default_x=120.93, default_y=-236.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=-14.32, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('1.Should')
                with Lyric(number='2', default_x=-16.13, default_y=-76.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.And')
                with Lyric(number='3', default_x=-15.68, default_y=-102.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.We')
                with Lyric(number='4', default_x=-16.58, default_y=-128.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('4.We')
                with Lyric(number='5', default_x=-16.13, default_y=-154.84, relative_y=-30.0):
                    Syllabic('single')
                    Text('5.And')
        with Measure(number='8', width=319.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=112.22, default_y=-221.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sure')
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('twa')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('twa')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text("there's")
            with Note(default_x=180.86, default_y=-221.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ac')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('hae')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('hae')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=222.16, default_y=-221.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('middle')
                    Text('quain')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text("ye'll")
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('run')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('paid')
                with Lyric(number='5', default_x=8.59, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('hand,')
            with Note(default_x=275.58, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('tance')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('end')
                    Text("l'd")
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='9', width=218.29):
            with Note(default_x=23.27, default_y=-216.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('bout')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trus')
            with Note(default_x=79.78, default_y=-221.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('pint')
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('ty')
            with Note(default_x=124.87, default_y=-216.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('got')
                with Lyric(number='2', default_x=8.88, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('stowp.')
                with Lyric(number='3', default_x=8.97, default_y=-97.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('braes,')
                with Lyric(number='4', default_x=8.99, default_y=-123.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('burn,')
                with Lyric(number='5', default_x=8.78, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('fiere.')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=181.39, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('frae')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
        with Measure(number='10', width=230.33):
            with Note(default_x=26.65, default_y=-221.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nev')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sure')
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('single')
                    Text("pu'd")
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('morn')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text("gie's")
            with Note(default_x=70.14, default_y=-221.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('er')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=137.17, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('brought')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text("I'll")
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gow')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('sun')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('hand')
            with Note(default_x=187.48, default_y=-201.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ans')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('till')
                with Lyric(number='5', default_x=8.38, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'")
        with Measure(number='11', width=185.56):
            with Note(default_x=26.01, default_y=-196.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=11.28, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('mind?')
                with Lyric(number='2', default_x=8.73, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('mine.')
                with Lyric(number='3', default_x=9.16, default_y=-97.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('fine;')
                with Lyric(number='4', default_x=9.35, default_y=-123.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('dine;')
                with Lyric(number='5', default_x=8.71, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('thine.')
            with Note(default_x=124.52, default_y=-186.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('Should')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text("And\xa0we'll")
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('single')
                    Text("But\xa0we've")
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('But')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
        with Measure(number='12', width=240.76):
            with Note(default_x=23.94, default_y=-201.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('tak')
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wan')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('seas')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text("we'll")
            with Note(default_x=93.09, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ac')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('end')
                    Text("der'd")
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('take')
            with Note(default_x=143.19, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('middle')
                    Text('quain')
                with Lyric(number='2', default_x=6.58, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('cup')
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('mony')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('tween')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=196.61, default_y=-221.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('tance')
                with Lyric(number='2', default_x=8.38, default_y=-71.96, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'")
                with Lyric(number='3', default_x=6.58, default_y=-97.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
                with Lyric(number='4', default_x=6.58, default_y=-123.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('us')
                with Lyric(number='5', default_x=6.58, default_y=-149.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('right')
        with Measure(number='13', width=317.72):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.01)
            with Note(default_x=80.4, default_y=-227.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-88.81, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kind')
                with Lyric(number='3', default_x=6.58, default_y=-114.78, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wea')
                with Lyric(number='4', default_x=6.58, default_y=-140.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('braid')
                with Lyric(number='5', default_x=6.58, default_y=-166.74, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gude')
            with Note(default_x=150.65, default_y=-232.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.83, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for')
                with Lyric(number='2', default_x=6.58, default_y=-88.81, relative_y=-30.0):
                    Syllabic('end')
                    Text('ness')
                with Lyric(number='3', default_x=6.58, default_y=-114.78, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry')
                with Lyric(number='4', default_x=6.58, default_y=-140.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('hae')
                with Lyric(number='5', default_x=6.58, default_y=-166.74, relative_y=-30.0):
                    Syllabic('middle')
                    Text('willie')
            with Note(default_x=213.07, default_y=-227.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.89, default_y=-62.83, relative_y=-30.0):
                    Syllabic('end')
                    Text('got,')
                with Lyric(number='2', default_x=6.58, default_y=-88.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('yet')
                with Lyric(number='3', default_x=8.9, default_y=-114.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('fit,')
                with Lyric(number='4', default_x=8.75, default_y=-140.76, relative_y=-30.0):
                    Syllabic('single')
                    Text("roar'd,")
                with Lyric(number='5', default_x=8.64, default_y=-166.74, relative_y=-30.0):
                    Syllabic('end')
                    Text('waught,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=283.32, default_y=-222.01):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-62.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
                with Lyric(number='2', default_x=6.58, default_y=-88.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
                with Lyric(number='3', default_x=8.49, default_y=-114.78, relative_y=-30.0):
                    Syllabic('single')
                    Text("sin'")
                with Lyric(number='4', default_x=8.49, default_y=-140.76, relative_y=-30.0):
                    Syllabic('single')
                    Text("sin'")
                with Lyric(number='5', default_x=6.58, default_y=-166.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
        with Measure(number='14', width=209.65):
            with Note(default_x=22.36, default_y=-232.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-62.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('days')
                with Lyric(number='2', default_y=-88.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
                with Lyric(number='3', default_y=-114.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
                with Lyric(number='4', default_y=-140.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
                with Lyric(number='5', default_y=-166.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
            with Note(default_x=87.75, default_y=-242.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.38, default_y=-62.83, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'")
            with Note(default_x=117.08, default_y=-242.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-62.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                with Lyric(number='2', default_y=-88.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
                with Lyric(number='3', default_y=-114.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
                with Lyric(number='4', default_y=-140.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
                with Lyric(number='5', default_y=-166.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
            with Note(default_x=167.81, default_y=-247.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-62.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
        with Measure(number='15', width=143.75):
            with Note(default_x=22.53, default_y=-232.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.89, default_y=-62.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
                with Lyric(number='2', default_x=8.89, default_y=-88.81, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
                with Lyric(number='3', default_x=8.89, default_y=-114.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
                with Lyric(number='4', default_x=8.89, default_y=-140.76, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
                with Lyric(number='5', default_x=8.89, default_y=-166.74, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='16', width=181.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=175.01):
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
                    with Dynamics(default_x=3.29, relative_y=20.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=140.63, default_y=-207.01):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-62.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('For')
        with Measure(number='18', width=167.02):
            with Note(default_x=21.69, default_y=-212.01):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-62.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
            with Note(default_x=47.56, default_y=-222.01):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=94.91, default_y=-222.01):
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
                with Lyric(number='1', default_y=-62.83, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
            with Note(default_x=142.25, default_y=-232.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='19', width=252.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.4, default_y=-216.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.12, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne,')
            with Note(default_x=131.82, default_y=-221.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
            with Note(default_x=166.66, default_y=-216.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.98, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('dear,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=218.08, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
        with Measure(number='20', width=155.72):
            with Note(default_x=21.69, default_y=-206.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
            with Note(default_x=47.56, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=89.26, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
            with Note(default_x=130.95, default_y=-201.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=165.19):
            with Note(default_x=22.53, default_y=-196.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.12, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=126.49, default_y=-186.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text("we'll")
        with Measure(number='22', width=147.57):
            with Note(default_x=16.95, default_y=-201.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('tak')
            with Note(default_x=49.03, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=81.11, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('cup')
            with Note(default_x=113.19, default_y=-221.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.38, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'")
        with Measure(number='23', width=198.62):
            with Note(default_x=23.04, default_y=-216.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.78, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kind')
            with Note(default_x=76.59, default_y=-221.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.78, relative_y=-30.0):
                    Syllabic('end')
                    Text('ness')
            with Note(default_x=110.67, default_y=-216.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('yet')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=164.22, default_y=-211.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
        with Measure(number='24', width=146.69):
            with Note(default_x=12.66, default_y=-221.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
            with Note(default_x=38.54, default_y=-231.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.23, default_y=-231.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
            with Note(default_x=121.93, default_y=-236.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='25', width=128.1):
            with Note(default_x=22.53, default_y=-221.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.89, default_y=-61.78, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='26', width=224.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=148.29):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=152.14):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=195.03):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=52.92)
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
            with Note(default_x=132.88, default_y=-236.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=-16.13, default_y=-50.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.And')
                with Lyric(number='2', default_x=-15.68, default_y=-76.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.We')
                with Lyric(number='3', default_x=-16.58, default_y=-102.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('4.We')
                with Lyric(number='4', default_x=-16.13, default_y=-128.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('5.And')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='30', width=115.62):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=52.92)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='31', width=130.57):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=115.62):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='33', width=112.61):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='34', width=332.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-121.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='35', width=260.48):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=229.03):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='37', width=232.43):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='38', width=140.09):
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
        with Measure(number='0', implicit='yes', width=136.89):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(178.44)
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
        with Measure(number='1', width=139.4):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='2', width=142.42):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=142.42):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='4', width=143.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='5', width=123.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=123.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=193.54):
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
            with Note(default_x=120.93, default_y=-429.44):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=-14.32, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('1.Should')
                with Lyric(number='2', default_x=-16.13, default_y=-65.98, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.And')
                with Lyric(number='3', default_x=-15.68, default_y=-91.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.We')
                with Lyric(number='4', default_x=-16.58, default_y=-117.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('4.We')
                with Lyric(number='5', default_x=-16.13, default_y=-143.9, relative_y=-30.0):
                    Syllabic('single')
                    Text('5.And')
        with Measure(number='8', width=319.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(180.5)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=112.22, default_y=-431.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sure')
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('twa')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('twa')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text("there's")
            with Note(default_x=180.86, default_y=-431.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ac')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('hae')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('hae')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=222.16, default_y=-431.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('middle')
                    Text('quain')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text("ye'll")
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('run')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('paid')
                with Lyric(number='5', default_x=8.59, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('hand,')
            with Note(default_x=275.58, default_y=-421.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('tance')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('end')
                    Text("l'd")
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='9', width=218.29):
            with Note(default_x=23.27, default_y=-426.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('bout')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trus')
            with Note(default_x=79.78, default_y=-431.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('pint')
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('ty')
            with Note(default_x=124.87, default_y=-426.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('got')
                with Lyric(number='2', default_x=8.88, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('stowp.')
                with Lyric(number='3', default_x=8.97, default_y=-102.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('braes,')
                with Lyric(number='4', default_x=8.99, default_y=-128.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('burn,')
                with Lyric(number='5', default_x=8.78, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('fiere.')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=181.39, default_y=-421.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('frae')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
        with Measure(number='10', width=230.33):
            with Note(default_x=26.65, default_y=-431.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nev')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sure')
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('single')
                    Text("pu'd")
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('morn')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text("gie's")
            with Note(default_x=70.14, default_y=-431.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('er')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=137.17, default_y=-421.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('brought')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text("I'll")
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gow')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('sun')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('hand')
            with Note(default_x=187.48, default_y=-431.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('end')
                    Text('ans')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('till')
                with Lyric(number='5', default_x=8.38, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'")
        with Measure(number='11', width=185.56):
            with Note(default_x=26.01, default_y=-426.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=11.28, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('mind?')
                with Lyric(number='2', default_x=8.73, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('mine.')
                with Lyric(number='3', default_x=9.16, default_y=-102.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('fine;')
                with Lyric(number='4', default_x=9.35, default_y=-128.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('dine;')
                with Lyric(number='5', default_x=8.71, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('thine.')
            with Note(default_x=124.52, default_y=-416.5):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('Should')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text("And\xa0we'll")
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('single')
                    Text("But\xa0we've")
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('But')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
        with Measure(number='12', width=240.76):
            with Note(default_x=23.94, default_y=-431.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('tak')
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wan')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('seas')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text("we'll")
            with Note(default_x=93.09, default_y=-421.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ac')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('end')
                    Text("der'd")
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('take')
            with Note(default_x=143.19, default_y=-421.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('middle')
                    Text('quain')
                with Lyric(number='2', default_x=6.58, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('cup')
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('mony')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('tween')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=196.61, default_y=-431.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.99, relative_y=-30.0):
                    Syllabic('end')
                    Text('tance')
                with Lyric(number='2', default_x=8.38, default_y=-76.96, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'")
                with Lyric(number='3', default_x=6.58, default_y=-102.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
                with Lyric(number='4', default_x=6.58, default_y=-128.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('us')
                with Lyric(number='5', default_x=6.58, default_y=-154.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('right')
        with Measure(number='13', width=317.72):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(194.85)
            with Note(default_x=80.4, default_y=-451.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-81.42, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kind')
                with Lyric(number='3', default_x=6.58, default_y=-107.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wea')
                with Lyric(number='4', default_x=6.58, default_y=-133.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('braid')
                with Lyric(number='5', default_x=6.58, default_y=-159.34, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gude')
            with Note(default_x=150.65, default_y=-456.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for')
                with Lyric(number='2', default_x=6.58, default_y=-81.42, relative_y=-30.0):
                    Syllabic('end')
                    Text('ness')
                with Lyric(number='3', default_x=6.58, default_y=-107.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry')
                with Lyric(number='4', default_x=6.58, default_y=-133.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('hae')
                with Lyric(number='5', default_x=6.58, default_y=-159.34, relative_y=-30.0):
                    Syllabic('middle')
                    Text('willie')
            with Note(default_x=213.07, default_y=-451.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.89, default_y=-55.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('got,')
                with Lyric(number='2', default_x=6.58, default_y=-81.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('yet')
                with Lyric(number='3', default_x=8.9, default_y=-107.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('fit,')
                with Lyric(number='4', default_x=8.75, default_y=-133.37, relative_y=-30.0):
                    Syllabic('single')
                    Text("roar'd,")
                with Lyric(number='5', default_x=8.64, default_y=-159.34, relative_y=-30.0):
                    Syllabic('end')
                    Text('waught,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=283.32, default_y=-456.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
                with Lyric(number='2', default_x=6.58, default_y=-81.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
                with Lyric(number='3', default_x=8.49, default_y=-107.39, relative_y=-30.0):
                    Syllabic('single')
                    Text("sin'")
                with Lyric(number='4', default_x=8.49, default_y=-133.37, relative_y=-30.0):
                    Syllabic('single')
                    Text("sin'")
                with Lyric(number='5', default_x=6.58, default_y=-159.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
        with Measure(number='14', width=209.65):
            with Note(default_x=22.36, default_y=-456.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('days')
                with Lyric(number='2', default_y=-81.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
                with Lyric(number='3', default_y=-107.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
                with Lyric(number='4', default_y=-133.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
                with Lyric(number='5', default_y=-159.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
            with Note(default_x=87.75, default_y=-451.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.38, default_y=-55.44, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'")
            with Note(default_x=117.08, default_y=-451.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                with Lyric(number='2', default_y=-81.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
                with Lyric(number='3', default_y=-107.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
                with Lyric(number='4', default_y=-133.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
                with Lyric(number='5', default_y=-159.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
            with Note(default_x=167.81, default_y=-456.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-55.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
        with Measure(number='15', width=143.75):
            with Note(default_x=22.53, default_y=-456.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.89, default_y=-55.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
                with Lyric(number='2', default_x=8.89, default_y=-81.42, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
                with Lyric(number='3', default_x=8.89, default_y=-107.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
                with Lyric(number='4', default_x=8.89, default_y=-133.37, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
                with Lyric(number='5', default_x=8.89, default_y=-159.34, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='16', width=181.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=175.01):
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
                    with Dynamics(default_x=3.29, relative_y=20.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=140.63, default_y=-451.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('For')
        with Measure(number='18', width=167.02):
            with Note(default_x=21.69, default_y=-456.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-55.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
            with Note(default_x=47.56, default_y=-446.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=94.91, default_y=-446.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
        with Measure(number='19', width=252.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.33)
            with Note(default_x=80.4, default_y=-335.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.12, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne,')
            with Note(default_x=131.82, default_y=-335.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
            with Note(default_x=166.66, default_y=-335.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('dear,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=218.08, default_y=-335.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
        with Measure(number='20', width=155.72):
            with Note(default_x=21.69, default_y=-335.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
            with Note(default_x=89.26, default_y=-335.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
            with Note(default_x=130.95, default_y=-345.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='21', width=165.19):
            with Note(default_x=22.53, default_y=-340.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.12, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=126.49, default_y=-330.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text("we'll")
        with Measure(number='22', width=147.57):
            with Note(default_x=16.95, default_y=-345.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('tak')
            with Note(default_x=49.03, default_y=-335.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=81.11, default_y=-335.33):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('cup')
            with Note(default_x=113.19, default_y=-345.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.38, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'")
        with Measure(number='23', width=198.62):
            with Note(default_x=23.04, default_y=-340.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.61, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kind')
            with Note(default_x=76.59, default_y=-345.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.61, relative_y=-30.0):
                    Syllabic('end')
                    Text('ness')
            with Note(default_x=110.67, default_y=-340.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('yet')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=164.22, default_y=-345.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
        with Measure(number='24', width=146.69):
            with Note(default_x=12.66, default_y=-345.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
            with Note(default_x=38.54, default_y=-340.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.23, default_y=-340.33):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
            with Note(default_x=121.93, default_y=-345.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='25', width=128.1):
            with Note(default_x=22.53, default_y=-345.33):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=8.89, default_y=-55.61, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='26', width=224.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(152.46)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=148.29):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=152.14):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=195.03):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=52.92)
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
            with Note(default_x=132.88, default_y=-403.46):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=-16.13, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.And')
                with Lyric(number='2', default_x=-15.68, default_y=-65.98, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.We')
                with Lyric(number='3', default_x=-16.58, default_y=-91.95, relative_y=-30.0):
                    Syllabic('single')
                    Text('4.We')
                with Lyric(number='4', default_x=-16.13, default_y=-117.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('5.And')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='30', width=115.62):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=52.92)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='31', width=130.57):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=115.62):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='33', width=112.61):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='34', width=332.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='35', width=260.48):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=229.03):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='37', width=232.43):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='38', width=140.09):
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
        with Measure(number='0', implicit='yes', width=136.89):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(159.75)
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
        with Measure(number='1', width=139.4):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='2', width=142.42):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=142.42):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='4', width=143.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='5', width=123.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=123.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=193.54):
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
            with Note(default_x=120.93, default_y=-614.19):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=-14.32, default_y=-40.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('1.Should')
                with Lyric(number='2', default_x=-16.13, default_y=-66.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.And')
                with Lyric(number='3', default_x=-15.68, default_y=-92.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.We')
                with Lyric(number='4', default_x=-16.58, default_y=-118.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('4.We')
                with Lyric(number='5', default_x=-16.13, default_y=-144.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('5.And')
        with Measure(number='8', width=319.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(183.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=112.22, default_y=-639.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sure')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('twa')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('twa')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text("there's")
            with Note(default_x=180.86, default_y=-639.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ac')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('hae')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('hae')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=222.16, default_y=-639.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('middle')
                    Text('quain')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text("ye'll")
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('run')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('paid')
                with Lyric(number='5', default_x=8.59, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('hand,')
            with Note(default_x=275.58, default_y=-639.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('tance')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('a')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('end')
                    Text("l'd")
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
        with Measure(number='9', width=218.29):
            with Note(default_x=23.27, default_y=-639.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('your')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('bout')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('in')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trus')
            with Note(default_x=79.78, default_y=-639.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('pint')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('ty')
            with Note(default_x=124.87, default_y=-639.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('got')
                with Lyric(number='2', default_x=8.88, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('stowp.')
                with Lyric(number='3', default_x=8.97, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('braes,')
                with Lyric(number='4', default_x=8.99, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('burn,')
                with Lyric(number='5', default_x=8.78, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('fiere.')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=181.39, default_y=-639.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('frae')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
        with Measure(number='10', width=230.33):
            with Note(default_x=26.65, default_y=-639.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('nev')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sure')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text("pu'd")
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('morn')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text("gie's")
            with Note(default_x=70.14, default_y=-639.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('er')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('ly')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('the')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('ing')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=137.17, default_y=-639.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('brought')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text("I'll")
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gow')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('sun')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('hand')
            with Note(default_x=187.48, default_y=-639.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('to')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('ans')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('till')
                with Lyric(number='5', default_x=8.38, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'")
        with Measure(number='11', width=185.56):
            with Note(default_x=26.01, default_y=-659.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=11.28, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('mind?')
                with Lyric(number='2', default_x=8.73, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('mine.')
                with Lyric(number='3', default_x=9.16, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('fine;')
                with Lyric(number='4', default_x=9.35, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('dine;')
                with Lyric(number='5', default_x=8.71, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('thine.')
            with Note(default_x=124.52, default_y=-659.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('Should')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text("And\xa0we'll")
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text("But\xa0we've")
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('But')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('And')
        with Measure(number='12', width=240.76):
            with Note(default_x=23.94, default_y=-654.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('tak')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wan')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('seas')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text("we'll")
            with Note(default_x=93.09, default_y=-654.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ac')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('end')
                    Text("der'd")
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('take')
            with Note(default_x=143.19, default_y=-654.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('middle')
                    Text('quain')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('cup')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('mony')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('end')
                    Text('tween')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=196.61, default_y=-654.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('tance')
                with Lyric(number='2', default_x=8.38, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'")
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('us')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('right')
        with Measure(number='13', width=317.72):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(189.95)
            with Note(default_x=80.4, default_y=-686.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('be')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kind')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wea')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('braid')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('gude')
            with Note(default_x=150.65, default_y=-686.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('for')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('end')
                    Text('ness')
                with Lyric(number='3', default_x=6.58, default_y=-93.49, relative_y=-30.0):
                    Syllabic('end')
                    Text('ry')
                with Lyric(number='4', default_x=6.58, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('hae')
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('middle')
                    Text('willie')
            with Note(default_x=213.07, default_y=-686.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.89, default_y=-41.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('got,')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('yet')
                with Lyric(number='3', default_x=8.9, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('fit,')
                with Lyric(number='4', default_x=8.75, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text("roar'd,")
                with Lyric(number='5', default_x=8.64, default_y=-145.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('waught,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=283.32, default_y=-671.81):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('and')
                with Lyric(number='2', default_x=6.58, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
                with Lyric(number='3', default_x=8.49, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text("sin'")
                with Lyric(number='4', default_x=8.49, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text("sin'")
                with Lyric(number='5', default_x=6.58, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
        with Measure(number='14', width=209.65):
            with Note(default_x=22.36, default_y=-671.81):
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
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('days')
                with Lyric(number='2', default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
                with Lyric(number='3', default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
                with Lyric(number='4', default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
                with Lyric(number='5', default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
            with Note(default_x=87.75, default_y=-691.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=8.38, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'")
            with Note(default_x=117.08, default_y=-691.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                with Lyric(number='2', default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
                with Lyric(number='3', default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
                with Lyric(number='4', default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
                with Lyric(number='5', default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
            with Note(default_x=167.81, default_y=-671.81):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
        with Measure(number='15', width=143.75):
            with Note(default_x=22.53, default_y=-671.81):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.89, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
                with Lyric(number='2', default_x=8.89, default_y=-67.51, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
                with Lyric(number='3', default_x=8.89, default_y=-93.49, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
                with Lyric(number='4', default_x=8.89, default_y=-119.46, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
                with Lyric(number='5', default_x=8.89, default_y=-145.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='16', width=181.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=175.01):
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
                    with Dynamics(default_x=6.58, relative_y=20.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=140.63, default_y=-691.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('For')
        with Measure(number='18', width=167.02):
            with Note(default_x=21.69, default_y=-671.81):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
            with Note(default_x=94.91, default_y=-671.81):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-41.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
        with Measure(number='19', width=252.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(84.25)
            with Note(default_x=80.4, default_y=-459.57):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=9.12, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne,')
            with Note(default_x=131.82, default_y=-464.57):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('my')
            with Note(default_x=166.66, default_y=-459.57):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=8.98, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('dear,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=218.08, default_y=-454.57):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
        with Measure(number='20', width=155.72):
            with Note(default_x=21.69, default_y=-449.57):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
            with Note(default_x=47.56, default_y=-454.57):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=89.26, default_y=-454.57):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
        with Measure(number='21', width=165.19):
            with Note(default_x=22.53, default_y=-474.57):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=9.12, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne,')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=126.49, default_y=-474.57):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text("we'll")
        with Measure(number='22', width=147.57):
            with Note(default_x=16.95, default_y=-469.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('tak')
            with Note(default_x=49.03, default_y=-469.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('a')
            with Note(default_x=81.11, default_y=-469.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('cup')
            with Note(default_x=113.19, default_y=-469.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=8.38, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text("o'")
        with Measure(number='23', width=198.62):
            with Note(default_x=23.04, default_y=-469.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-57.91, relative_y=-30.0):
                    Syllabic('begin')
                    Text('kind')
            with Note(default_x=76.59, default_y=-469.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-57.91, relative_y=-30.0):
                    Syllabic('end')
                    Text('ness')
            with Note(default_x=110.67, default_y=-469.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('yet')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=164.22, default_y=-454.57):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('for')
        with Measure(number='24', width=146.69):
            with Note(default_x=12.66, default_y=-464.57):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('auld')
                    Extend()
            with Note(default_x=38.54, default_y=-474.57):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.23, default_y=-474.57):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('lang')
                    Extend()
            with Note(default_x=121.93, default_y=-454.57):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='25', width=128.1):
            with Note(default_x=22.53, default_y=-454.57):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Lyric(number='1', default_x=8.89, default_y=-57.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('syne.')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
        with Measure(number='26', width=224.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(133.78)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=148.29):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=152.14):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=195.03):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=52.92)
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
            with Note(default_x=132.88, default_y=-562.24):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=-16.13, default_y=-40.99, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.And')
                with Lyric(number='2', default_x=-15.68, default_y=-66.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.We')
                with Lyric(number='3', default_x=-16.58, default_y=-92.94, relative_y=-30.0):
                    Syllabic('single')
                    Text('4.We')
                with Lyric(number='4', default_x=-16.13, default_y=-118.91, relative_y=-30.0):
                    Syllabic('single')
                    Text('5.And')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='30', width=115.62):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=52.92)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='31', width=130.57):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=115.62):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='33', width=112.61):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='34', width=332.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='35', width=260.48):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=229.03):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='37', width=232.43):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='38', width=140.09):
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
        with Measure(number='0', implicit='yes', width=136.89):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(170.88)
                with StaffLayout(number=2):
                    StaffDistance(51.52)
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
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=101.55, default_y=-832.57):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=101.55, default_y=-825.57):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=101.55, default_y=-926.08):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=101.55, default_y=-901.58):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='1', width=139.4):
            with Note(default_x=12.66, default_y=-832.57):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-815.07):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=60.51, default_y=-832.57):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=60.51, default_y=-815.07):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=78.91, default_y=-832.57):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=78.91, default_y=-815.07):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=108.36, default_y=-815.07):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=108.36, default_y=-808.07):
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
            with Note(default_x=12.66, default_y=-926.08):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-901.58):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=60.51, default_y=-926.08):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=60.51, default_y=-901.58):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=78.91, default_y=-926.08):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=78.91, default_y=-901.58):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=108.36, default_y=-926.08):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=108.36, default_y=-901.58):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='2', width=142.42):
            with Note(default_x=12.66, default_y=-815.07):
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
            with Note(default_x=12.66, default_y=-804.57):
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
            with Note(default_x=61.66, default_y=-815.07):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=61.66, default_y=-808.07):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=80.51, default_y=-815.07):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=80.51, default_y=-804.57):
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
            with Note(default_x=110.66, default_y=-815.07):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=110.66, default_y=-797.57):
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
            with Note(default_x=12.66, default_y=-933.08):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-908.58):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=61.66, default_y=-936.58):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=61.66, default_y=-912.08):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=80.51, default_y=-933.08):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=80.51, default_y=-908.58):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=110.66, default_y=-940.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=110.66, default_y=-915.58):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='3', width=142.42):
            with Note(default_x=12.66, default_y=-815.07):
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
            with Note(default_x=12.66, default_y=-801.07):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=61.66, default_y=-815.07):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=61.66, default_y=-801.07):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=80.51, default_y=-815.07):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=80.51, default_y=-801.07):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=110.66, default_y=-808.07):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=110.66, default_y=-790.57):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=12.66, default_y=-943.58):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-919.08):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=61.66, default_y=-943.58):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=61.66, default_y=-919.08):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=80.51, default_y=-943.58):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=80.51, default_y=-919.08):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=110.66, default_y=-950.58):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=110.66, default_y=-926.08):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='4', width=143.05):
            with Note(default_x=12.66, default_y=-818.57):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-811.57):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=61.9, default_y=-818.57):
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
            with Note(default_x=61.9, default_y=-811.57):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=80.84, default_y=-818.57):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=80.84, default_y=-811.57):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=111.15, default_y=-832.57):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=12.66, default_y=-936.58):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-912.08):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=61.9, default_y=-936.58):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=61.9, default_y=-912.08):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=80.84, default_y=-936.58):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=80.84, default_y=-912.08):
                Chord()
                with Pitch():
                    Step('C')
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
        with Measure(number='5', width=123.7):
            with Note(default_x=12.66, default_y=-850.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-836.07):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=47.0, default_y=-850.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=47.0, default_y=-836.07):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=64.6, default_y=-912.08):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=64.6, default_y=-898.08):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=98.94, default_y=-912.08):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=98.94, default_y=-898.08):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=123.7):
            with Note(default_x=12.66, default_y=-850.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-836.07):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=47.0, default_y=-850.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=47.0, default_y=-836.07):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=64.6, default_y=-912.08):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=64.6, default_y=-898.08):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=98.94, default_y=-912.08):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=98.94, default_y=-898.08):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=193.54):
            with Note(default_x=12.66, default_y=-843.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-825.57):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=66.79, default_y=-843.07):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=66.79, default_y=-825.57):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=87.61, default_y=-839.57):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=120.93, default_y=-832.57):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=120.93, default_y=-825.57):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=66.79, default_y=-912.08):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=66.79, default_y=-898.08):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=87.61, default_y=-901.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=87.61, default_y=-894.58):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=120.93, default_y=-901.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='8', width=319.42):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(189.18)
                with StaffLayout(number=2):
                    StaffDistance(45.5)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=112.22, default_y=-876.18):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=112.22, default_y=-858.68):
                Chord()
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
            with Note(default_x=222.16, default_y=-876.18):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=222.16, default_y=-858.68):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=275.58, default_y=-869.18):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=275.58, default_y=-851.68):
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
            with Note(default_x=112.22, default_y=-963.68):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=112.22, default_y=-939.18):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=222.16, default_y=-963.68):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=222.16, default_y=-939.18):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=275.58, default_y=-963.68):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=275.58, default_y=-939.18):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=218.29):
            with Note(default_x=23.27, default_y=-872.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=23.27, default_y=-855.18):
                Chord()
                with Pitch():
                    Step('G')
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
            with Note(default_x=124.87, default_y=-872.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=124.87, default_y=-855.18):
                Chord()
                with Pitch():
                    Step('G')
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
            with Note(default_x=23.27, default_y=-974.18):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=23.27, default_y=-949.68):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=124.87, default_y=-974.18):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=124.87, default_y=-949.68):
                Chord()
                with Pitch():
                    Step('C')
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
        with Measure(number='10', width=230.33):
            with Note(default_x=26.65, default_y=-876.18):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=26.65, default_y=-858.68):
                Chord()
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
            with Note(default_x=137.17, default_y=-858.68):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.17, default_y=-851.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=187.48, default_y=-851.68):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=187.48, default_y=-844.68):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=26.65, default_y=-963.68):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=26.65, default_y=-939.18):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=137.17, default_y=-963.68):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=137.17, default_y=-939.18):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=187.48, default_y=-963.68):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=187.48, default_y=-939.18):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='11', width=185.56):
            with Note(default_x=26.01, default_y=-848.18):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=26.01, default_y=-841.18):
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
            with Note(default_x=124.52, default_y=-841.18):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=124.52, default_y=-834.18):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=26.01, default_y=-977.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=26.01, default_y=-953.18):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=124.52, default_y=-977.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=124.52, default_y=-953.18):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='12', width=240.76):
            with Note(default_x=23.94, default_y=-851.68):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=23.94, default_y=-844.68):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=143.19, default_y=-858.68):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=143.19, default_y=-851.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=196.61, default_y=-876.18):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=196.61, default_y=-858.68):
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
            with Note(default_x=23.94, default_y=-974.18):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=23.94, default_y=-949.68):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=143.19, default_y=-974.18):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=143.19, default_y=-949.68):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=196.61, default_y=-974.18):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=196.61, default_y=-949.68):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='13', width=317.72):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(173.29)
                with StaffLayout(number=2):
                    StaffDistance(45.5)
            with Note(default_x=80.4, default_y=-889.1):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=80.4, default_y=-871.6):
                Chord()
                with Pitch():
                    Step('G')
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
            with Note(default_x=213.07, default_y=-889.1):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=213.07, default_y=-871.6):
                Chord()
                with Pitch():
                    Step('G')
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
            with Note(default_x=80.4, default_y=-990.6):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=80.4, default_y=-966.1):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=213.07, default_y=-990.6):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=213.07, default_y=-966.1):
                Chord()
                with Pitch():
                    Step('C')
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
        with Measure(number='14', width=209.65):
            with Note(default_x=22.36, default_y=-892.6):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=22.36, default_y=-875.1):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=87.75, default_y=-889.1):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=87.75, default_y=-882.1):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=117.08, default_y=-889.1):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=117.08, default_y=-882.1):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=167.81, default_y=-892.6):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=167.81, default_y=-885.6):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=22.36, default_y=-980.1):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=22.36, default_y=-955.6):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=87.75, default_y=-994.1):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=87.75, default_y=-969.6):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=117.08, default_y=-994.1):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=117.08, default_y=-969.6):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=167.81, default_y=-980.1):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=167.81, default_y=-955.6):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='15', width=143.75):
            with Note(default_x=22.53, default_y=-892.6):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=22.53, default_y=-875.1):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=71.69, default_y=-892.6):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=71.69, default_y=-875.1):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=87.36, default_y=-885.6):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.02, default_y=-882.1):
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
            with Note(default_x=121.41, default_y=-878.6):
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
            with Backup():
                Duration(8.0)
            with Note(default_x=22.53, default_y=-980.1):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=22.53, default_y=-955.6):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='16', width=181.23):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=12.66, default_y=-875.1):
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
            with Note(default_x=74.29, default_y=-882.1):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=94.83, default_y=-882.1):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=135.92, default_y=-885.6):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=74.29, default_y=-962.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=94.83, default_y=-962.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=135.92, default_y=-966.1):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='17', width=175.01):
            with Note(default_x=10.94, default_y=-882.1):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=50.84, default_y=-885.6):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=90.73, default_y=-882.1):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=140.63, default_y=-864.6):
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
            with Note(default_x=140.63, default_y=-857.6):
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
            with Note(default_x=10.94, default_y=-962.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=50.84, default_y=-966.1):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=90.73, default_y=-962.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=140.63, default_y=-969.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=140.63, default_y=-945.1):
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
        with Measure(number='18', width=167.02):
            with Note(default_x=21.69, default_y=-868.1):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=21.69, default_y=-861.1):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=94.91, default_y=-885.6):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=94.91, default_y=-868.1):
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
            with Backup():
                Duration(8.0)
            with Note(default_x=21.69, default_y=-980.1):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=21.69, default_y=-955.6):
                Chord()
                with Pitch():
                    Step('F')
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
            with Note(default_x=94.91, default_y=-980.1):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=94.91, default_y=-955.6):
                Chord()
                with Pitch():
                    Step('F')
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
        with Measure(number='19', width=252.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(101.65)
                with StaffLayout(number=2):
                    StaffDistance(45.5)
            with Note(default_x=80.4, default_y=-596.73):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=80.4, default_y=-582.73):
                Chord()
                with Pitch():
                    Step('G')
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
            with Note(default_x=166.66, default_y=-596.73):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=166.66, default_y=-582.73):
                Chord()
                with Pitch():
                    Step('G')
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
            with Note(default_x=80.4, default_y=-694.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=80.4, default_y=-670.23):
                Chord()
                with Pitch():
                    Step('E')
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
            with Note(default_x=166.66, default_y=-694.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=166.66, default_y=-670.23):
                Chord()
                with Pitch():
                    Step('E')
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
        with Measure(number='20', width=155.72):
            with Note(default_x=21.69, default_y=-596.73):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=21.69, default_y=-575.73):
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
            with Note(default_x=89.26, default_y=-596.73):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=89.26, default_y=-575.73):
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
            with Note(default_x=130.95, default_y=-579.23):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=130.95, default_y=-572.23):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=21.69, default_y=-687.73):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=21.69, default_y=-663.23):
                Chord()
                with Pitch():
                    Step('G')
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
            with Note(default_x=89.26, default_y=-691.23):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=89.26, default_y=-666.73):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=130.95, default_y=-691.23):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=130.95, default_y=-666.73):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='21', width=165.19):
            with Note(default_x=22.53, default_y=-575.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=22.53, default_y=-568.73):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=75.38, default_y=-575.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=92.41, default_y=-572.23):
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
            with Note(default_x=109.45, default_y=-568.73):
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
            with Note(default_x=126.49, default_y=-568.73):
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
            with Note(default_x=126.49, default_y=-561.73):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=22.53, default_y=-680.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=22.53, default_y=-666.73):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=109.45, default_y=-680.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=109.45, default_y=-656.23):
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
        with Measure(number='22', width=147.57):
            with Note(default_x=16.95, default_y=-579.23):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=16.95, default_y=-572.23):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=49.03, default_y=-586.23):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=49.03, default_y=-579.23):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=81.11, default_y=-586.23):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=81.11, default_y=-579.23):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=113.19, default_y=-603.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=113.19, default_y=-586.23):
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
            with Note(default_x=16.95, default_y=-677.23):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=16.95, default_y=-652.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=49.03, default_y=-677.23):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=49.03, default_y=-652.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=81.11, default_y=-677.23):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=81.11, default_y=-652.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=113.19, default_y=-677.23):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=113.19, default_y=-652.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=198.62):
            with Note(default_x=23.04, default_y=-600.23):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=23.04, default_y=-582.73):
                Chord()
                with Pitch():
                    Step('G')
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
            with Note(default_x=110.67, default_y=-600.23):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=110.67, default_y=-582.73):
                Chord()
                with Pitch():
                    Step('G')
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
            with Note(default_x=23.04, default_y=-701.73):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=23.04, default_y=-677.23):
                Chord()
                with Pitch():
                    Step('C')
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
            with Note(default_x=110.67, default_y=-701.73):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=110.67, default_y=-677.23):
                Chord()
                with Pitch():
                    Step('C')
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
        with Measure(number='24', width=146.69):
            with Note(default_x=12.66, default_y=-603.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=12.66, default_y=-586.23):
                Chord()
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
            with Note(default_x=80.23, default_y=-600.23):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=80.23, default_y=-593.23):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=121.93, default_y=-603.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=121.93, default_y=-596.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=12.66, default_y=-698.23):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=12.66, default_y=-673.73):
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
            with Note(default_x=80.23, default_y=-705.23):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=80.23, default_y=-680.73):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=121.93, default_y=-691.23):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=121.93, default_y=-666.73):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='25', width=128.1):
            with Note(default_x=22.53, default_y=-603.73):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=22.53, default_y=-586.23):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=87.67, default_y=-617.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=103.34, default_y=-614.23):
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
            with Backup():
                Duration(8.0)
            with Note(default_x=22.53, default_y=-691.23):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=22.53, default_y=-666.73):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='26', width=224.49):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(134.64)
                with StaffLayout(number=2):
                    StaffDistance(57.82)
            with Note(default_x=80.4, default_y=-751.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=99.64, default_y=-758.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=149.69, default_y=-758.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=199.73, default_y=-761.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(8.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=118.89, default_y=-833.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=149.69, default_y=-833.7):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=180.48, default_y=-830.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='27', width=148.29):
            with Note(default_x=12.66, default_y=-751.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=59.15, default_y=-754.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=77.03, default_y=-744.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=123.52, default_y=-747.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(8.0)
            with Note(default_x=12.66, default_y=-826.7):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.27, default_y=-830.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=77.03, default_y=-819.7):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=105.64, default_y=-823.2):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='28', width=152.14):
            with Note(default_x=12.66, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-726.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=57.56, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=57.56, default_y=-730.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=86.1, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=86.1, default_y=-719.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=127.38, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=127.38, default_y=-723.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=12.66, default_y=-812.7):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.06, default_y=-816.2):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=86.1, default_y=-847.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=111.5, default_y=-826.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='29', width=195.03):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=52.92)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=31.26, default_y=-723.39):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.59, default_y=-730.39):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.91, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=92.23, default_y=-740.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.56, default_y=-744.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.88, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.21, default_y=-740.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(8.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('5')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='30', width=115.62):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=52.92)
            with Note(default_x=12.66, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-726.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=44.6, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=44.6, default_y=-726.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=61.63, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=61.63, default_y=-726.89):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=87.83, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=87.83, default_y=-719.89):
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
            with Note(default_x=12.66, default_y=-830.2):
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
            with Note(default_x=44.6, default_y=-830.2):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=61.63, default_y=-830.2):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=87.83, default_y=-837.2):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='31', width=130.57):
            with Note(default_x=12.66, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-723.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=46.57, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=46.57, default_y=-723.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=63.95, default_y=-737.39):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=63.95, default_y=-723.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=91.76, default_y=-723.39):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=91.76, default_y=-716.39):
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
            with Backup():
                Duration(8.0)
            with Note(default_x=12.66, default_y=-847.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=46.57, default_y=-847.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=63.95, default_y=-847.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=91.76, default_y=-847.7):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='32', width=115.62):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=12.66, default_y=-726.89):
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
            with Note(default_x=12.66, default_y=-719.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=44.6, default_y=-730.39):
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
            with Note(default_x=44.6, default_y=-723.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=61.63, default_y=-726.89):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=61.63, default_y=-719.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=87.83, default_y=-726.89):
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
                    Fermata(None, type='upright', default_y=24.42, relative_y=10.0)
            with Note(default_x=87.83, default_y=-716.39):
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
            with Note(default_x=87.83, default_y=-709.39):
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
            with Note(default_x=12.66, default_y=-802.2):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=44.6, default_y=-826.7):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=44.6, default_y=-802.2):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=61.63, default_y=-826.7):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=61.63, default_y=-802.2):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=87.83, default_y=-833.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Fermata(None, type='upright', default_y=4.42, relative_y=10.0)
            with Note(default_x=87.83, default_y=-809.2):
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
        with Measure(number='33', width=112.61):
            with Note(default_x=12.66, default_y=-740.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.85, default_y=-747.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=59.84, default_y=-747.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=85.42, default_y=-754.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('5')
                Staff(2)
        with Measure(number='34', width=332.34):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(199.82)
                with StaffLayout(number=2):
                    StaffDistance(64.1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=111.69, default_y=-234.82):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.98, default_y=-227.82):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.28, default_y=-220.82):
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
            with Note(default_x=205.57, default_y=-227.82):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=236.86, default_y=-220.82):
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
            with Note(default_x=268.16, default_y=-213.82):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=299.45, default_y=-210.32):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(8.0)
            with Note(default_x=80.4, default_y=-288.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=174.28, default_y=-295.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=205.57, default_y=-295.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=268.16, default_y=-302.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='35', width=260.48):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=43.44, default_y=-224.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=74.21, default_y=-217.32):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.99, default_y=-210.32):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.77, default_y=-217.32):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=166.55, default_y=-210.32):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.32, default_y=-203.32):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.1, default_y=-199.82):
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
            with Note(default_x=12.66, default_y=-309.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=104.99, default_y=-316.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=135.77, default_y=-316.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=197.32, default_y=-323.42):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='36', width=229.03):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=42.49, default_y=-203.32):
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
            with Note(default_x=72.32, default_y=-196.32):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.15, default_y=-189.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=131.98, default_y=-189.32):
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
            with Note(default_x=131.98, default_y=-178.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=179.7, default_y=-192.82):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=179.7, default_y=-175.32):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=12.66, default_y=-309.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=102.15, default_y=-309.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=102.15, default_y=-295.42):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=131.98, default_y=-309.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=131.98, default_y=-295.42):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=179.7, default_y=-323.42):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=179.7, default_y=-298.92):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='37', width=232.43):
            with Note(default_x=12.66, default_y=-192.82):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=12.66, default_y=-175.32):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=44.05, default_y=-192.82):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=44.05, default_y=-175.32):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=138.21, default_y=-196.32):
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
            with Note(default_x=138.21, default_y=-189.32):
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
            with Note(default_x=199.45, default_y=-199.82):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=199.45, default_y=-192.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(8.0)
            with Note(default_x=12.66, default_y=-330.42):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=12.66, default_y=-305.92):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=75.44, default_y=-333.92):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=75.44, default_y=-309.42):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=138.21, default_y=-337.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=138.21, default_y=-312.92):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=199.45, default_y=-323.42):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=199.45, default_y=-298.92):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='38', width=140.09):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=12.66, default_y=-199.82):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=34.42, relative_y=10.0)
            with Note(default_x=12.66, default_y=-175.32):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.66, default_y=-323.42):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', default_y=13.4, relative_y=10.0)
            with Note(default_x=12.66, default_y=-298.92):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')