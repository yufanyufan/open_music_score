with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('chuunckey ghazz rithems')
    with Identification():
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(7.05556)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1683.36)
            PageWidth(1190.88)
            with PageMargins(type='even'):
                LeftMargin(56.6929)
                RightMargin(56.6929)
                TopMargin(56.6929)
                BottomMargin(113.386)
            with PageMargins(type='odd'):
                LeftMargin(56.6929)
                RightMargin(56.6929)
                TopMargin(56.6929)
                BottomMargin(113.386)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('chuunckey ghazz rithems', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Soprano')
            PartAbbreviation('S.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Alto')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Tenor')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Bass')
            PartAbbreviation('B.')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=394.85):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(93.8)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-39.8, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('150')
                Sound(tempo=150.0)
            with Note(default_x=103.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=176.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=248.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=284.65, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=320.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=357.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=307.45):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='3', width=281.39):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='4', width=297.85):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(37.8)
                        RightMargin(0.0)
                    SystemDistance(104.14)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=169.67):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='6', width=159.55):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='7', width=103.16):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='8', width=103.16):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=103.16):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='10', width=103.16):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='11', width=112.47):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(37.8)
                        RightMargin(-0.0)
                    SystemDistance(104.14)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='12', width=84.23):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
        with Measure(number='13', width=100.82):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='14', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='15', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='16', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='18', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='19', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='20', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='21', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='22', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='23', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='24', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='25', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='26', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=219.43):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(37.8)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='30', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='31', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=394.85):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=103.63, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=103.63, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=176.04, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=176.04, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=284.65, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=320.85, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=357.05, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=307.45):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=49.55, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=122.78, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=196.01, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='3', width=281.39):
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=81.8, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=180.79, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=213.79, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=246.79, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='4', width=297.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=106.78, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=160.92, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=215.05, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=242.12, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=269.19, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='5', width=169.67):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=32.79, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.64, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=72.5, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=92.35, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='6', width=159.55):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
        with Measure(number='7', width=103.16):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='8', width=103.16):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='9', width=103.16):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='10', width=103.16):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='11', width=112.47):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='12', width=84.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='13', width=100.82):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='14', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='15', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='16', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='18', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='19', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='20', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='21', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='22', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='23', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='24', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='25', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='26', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=219.43):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='30', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='31', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=394.85):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note(default_x=103.63, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=248.44, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=284.65, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=357.05, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='2', width=307.45):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=49.55, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=122.78, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=196.01, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='3', width=281.39):
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='4', width=297.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='5', width=169.67):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=159.55):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=103.16):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='8', width=103.16):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='9', width=103.16):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='10', width=103.16):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='11', width=112.47):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='12', width=84.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='13', width=100.82):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='14', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='15', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='16', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='18', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='19', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='20', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='21', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='22', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='23', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='24', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='25', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='26', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=219.43):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='30', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='31', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=394.85):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=103.63, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=248.44, default_y=-375.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=320.85, default_y=-375.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='2', width=307.45):
            with Note(default_x=12.94, default_y=-360.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=86.17, default_y=-365.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=159.39, default_y=-365.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=232.62, default_y=-370.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
        with Measure(number='3', width=281.39):
            with Note(default_x=15.8, default_y=-375.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=147.79, default_y=-390.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=246.79, default_y=-375.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='4', width=297.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=106.78, default_y=-370.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=160.92, default_y=-365.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=215.05, default_y=-365.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=242.12, default_y=-335.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=269.19, default_y=-340.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=169.67):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=159.55):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=103.16):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='8', width=103.16):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='9', width=103.16):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='10', width=103.16):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='11', width=112.47):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='12', width=84.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='13', width=100.82):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='14', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='15', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='16', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='18', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='19', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='20', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='21', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='22', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='23', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='24', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='25', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='26', width=57.09):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=219.43):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='30', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='31', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=164.05):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')