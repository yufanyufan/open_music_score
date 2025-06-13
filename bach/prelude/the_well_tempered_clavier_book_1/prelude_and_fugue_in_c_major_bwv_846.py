with ScorePartwise(version='3.1'):
    with Identification():
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
            Millimeters(7.05556)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1683.78)
            PageWidth(1190.55)
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
    with PartList():
        with ScorePart(id='P1'):
            PartName('Piano, upper')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Piano, lower')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=509.66):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(131.2)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Attributes():
                Divisions(4.0)
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
                    with Metronome(parentheses='no', default_x=-55.38, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Sound(tempo=60.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=149.81, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=175.4, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=200.99, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=226.58, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=252.17, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=277.76, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=354.53, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=380.11, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=405.7, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=431.29, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=456.88, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=482.47, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='2', width=436.3):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=68.48, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=94.64, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=120.8, default_y=0.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=146.96, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=173.11, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=199.27, default_y=0.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=277.75, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=303.91, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=330.07, default_y=0.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=356.23, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=382.39, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=408.55, default_y=0.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='3', width=540.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    SystemDistance(210.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=121.92, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=151.7, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=181.48, default_y=0.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=211.26, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=241.04, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=270.82, default_y=0.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=360.16, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=389.94, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=419.72, default_y=0.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=449.5, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=479.28, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=509.06, default_y=0.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='4', width=485.12):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=74.58, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=103.79, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=133.0, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=162.21, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=191.42, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=220.63, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=308.26, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=337.47, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=366.68, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=395.89, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=425.1, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=454.31, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='5', width=531.25):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(0.0)
                    SystemDistance(210.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=120.77, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=149.98, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=179.18, default_y=10.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=208.39, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=237.59, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=266.8, default_y=10.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=354.42, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=383.62, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=412.83, default_y=10.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=442.03, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=471.24, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=500.44, default_y=10.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='6', width=494.31):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F♯', relative_y=44.0)
            with Note(default_x=75.73, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=105.51, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=135.3, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F♯', relative_y=44.0)
            with Note(default_x=165.08, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=194.87, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=224.65, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F♯', relative_y=44.0)
            with Note(default_x=314.01, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=343.79, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=373.58, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F♯', relative_y=44.0)
            with Note(default_x=403.36, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=433.14, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=462.93, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='7', width=531.25):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    SystemDistance(210.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=120.77, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=149.98, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=179.18, default_y=5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=208.39, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=237.59, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=266.8, default_y=5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=354.42, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=383.62, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=412.83, default_y=5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=442.03, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=471.24, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=500.44, default_y=5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='8', width=494.31):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=75.73, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=105.51, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=135.3, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=165.08, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=194.87, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=224.65, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=314.01, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=343.79, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=373.58, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=403.36, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=433.14, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=462.93, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='9', width=525.54):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=120.06, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=148.91, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=177.76, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=206.6, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=235.45, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=264.3, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=350.85, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=379.7, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=408.55, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=437.39, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=466.24, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=495.09, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=500.02):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=96.16, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F♯', relative_y=44.0)
            with Note(default_x=126.06, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=154.7, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=183.34, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F♯', relative_y=44.0)
            with Note(default_x=211.99, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=240.63, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=326.56, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F♯', relative_y=44.0)
            with Note(default_x=355.21, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=383.85, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=412.49, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F♯', relative_y=44.0)
            with Note(default_x=441.14, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=469.78, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='11', width=520.08):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(0.0)
                    SystemDistance(210.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=117.43, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=146.07, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=174.72, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=203.37, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=232.01, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=260.66, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=346.6, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=375.25, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=403.89, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=432.54, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=461.18, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=489.83, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=505.49):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=74.41, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=105.09, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C♯', relative_y=44.0)
            with Note(default_x=135.76, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=166.44, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=197.12, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C♯', relative_y=44.0)
            with Note(default_x=227.79, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=319.82, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=350.5, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C♯', relative_y=44.0)
            with Note(default_x=381.18, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=411.86, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=442.53, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C♯', relative_y=44.0)
            with Note(default_x=473.21, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='13', width=528.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    SystemDistance(210.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=119.07, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=148.19, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=177.31, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=206.43, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=235.55, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=264.67, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=352.03, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=381.15, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=410.27, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=439.39, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=468.51, default_y=-25.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=497.63, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=497.22):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=73.38, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=103.54, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=133.7, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=163.86, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=194.02, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=224.18, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=314.66, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=344.82, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=374.98, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=405.14, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=435.3, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=465.46, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='15', width=518.43):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    SystemDistance(210.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=117.83, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=146.33, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=174.83, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=203.33, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=231.83, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=260.33, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=345.83, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=374.33, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=402.83, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=431.33, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=459.83, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=488.33, default_y=-15.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='16', width=507.14):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=74.62, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=105.4, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=136.18, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=166.96, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=197.74, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=228.52, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=320.86, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=351.64, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=382.42, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=413.2, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=443.98, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=474.76, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='17', width=537.1):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=120.16, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=149.83, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=179.5, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=209.16, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=238.83, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=268.5, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=357.5, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=387.17, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=416.83, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=446.5, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=476.17, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=505.83, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='18', width=488.46):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=72.28, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=101.89, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=131.51, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=161.12, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=190.73, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=220.35, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=309.19, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=338.8, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=368.41, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=398.02, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=427.64, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=457.25, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=537.1):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    SystemDistance(210.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=120.16, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=149.83, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=179.5, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=209.16, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=238.83, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=268.5, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=357.5, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=387.17, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=416.83, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=446.5, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=476.17, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=505.83, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='20', width=488.46):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B♭', relative_y=44.0)
            with Note(default_x=72.28, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=101.89, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=131.51, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B♭', relative_y=44.0)
            with Note(default_x=161.12, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=190.73, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=220.35, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B♭', relative_y=44.0)
            with Note(default_x=309.19, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=338.8, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=368.41, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B♭', relative_y=44.0)
            with Note(default_x=398.02, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=427.64, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=457.25, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='21', width=526.3):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(0.0)
                    SystemDistance(210.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=118.81, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=147.8, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=176.8, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=205.79, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=234.78, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=263.77, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=350.75, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=379.74, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=408.73, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=437.72, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=466.72, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=495.71, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=499.26):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=77.92, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=107.9, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E♭', relative_y=44.0)
            with Note(default_x=137.88, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=167.86, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=197.84, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E♭', relative_y=44.0)
            with Note(default_x=227.83, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=317.77, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=347.75, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E♭', relative_y=44.0)
            with Note(default_x=377.74, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=407.72, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=437.7, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E♭', relative_y=44.0)
            with Note(default_x=467.68, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=543.0):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    SystemDistance(210.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=130.83, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=160.15, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=189.48, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=218.81, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=248.13, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=277.46, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=365.44, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=394.77, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=424.1, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=453.42, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=482.75, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=512.08, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=482.56):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Attributes():
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=77.48, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=104.69, default_y=5.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=131.9, default_y=15.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=159.12, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=186.33, default_y=5.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=213.54, default_y=15.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=295.17, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=322.39, default_y=5.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=349.6, default_y=15.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=376.81, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=404.02, default_y=5.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Attributes():
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=453.75, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='25', width=536.67):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=120.11, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=149.75, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=179.39, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=209.03, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=238.67, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=268.31, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=357.23, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=386.87, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=416.51, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=446.15, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=475.79, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=505.43, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=488.9):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=72.34, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=101.98, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=131.62, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=161.26, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=190.9, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=220.54, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=309.46, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=339.1, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=368.74, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=398.38, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=428.02, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=457.66, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=519.24):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    SystemDistance(210.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=117.93, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=146.48, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=175.03, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=203.58, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=232.13, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=260.68, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=346.34, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=374.89, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=403.44, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=431.99, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=460.54, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=489.09, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=506.32):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=74.41, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=105.09, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F♯', relative_y=44.0)
            with Note(default_x=136.59, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=167.27, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=197.95, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F♯', relative_y=44.0)
            with Note(default_x=228.63, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=320.66, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=351.33, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F♯', relative_y=44.0)
            with Note(default_x=382.01, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=412.69, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=443.37, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F♯', relative_y=44.0)
            with Note(default_x=474.04, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=536.67):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    SystemDistance(210.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=120.11, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=149.75, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=179.39, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=209.03, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=238.67, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=268.31, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=357.23, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=386.87, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=416.51, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=446.15, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=475.79, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=505.43, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='30', width=488.9):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=72.34, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=101.98, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=131.62, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=161.26, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=190.9, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=220.54, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=309.46, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=339.1, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=368.74, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=398.38, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=428.02, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=457.66, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='31', width=531.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    SystemDistance(210.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=119.44, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=148.75, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=178.05, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=207.36, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=236.67, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=265.97, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=353.89, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=383.2, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=412.51, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=441.81, default_y=-65.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=471.12, default_y=-55.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=500.43, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='32', width=494.23):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Attributes():
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=84.47, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B♭', relative_y=44.0)
            with Note(default_x=113.62, default_y=5.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=142.78, default_y=20.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=171.93, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B♭', relative_y=44.0)
            with Note(default_x=201.09, default_y=5.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=230.24, default_y=20.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=317.7, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B♭', relative_y=44.0)
            with Note(default_x=346.86, default_y=5.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=376.01, default_y=20.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=405.17, default_y=-5.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B♭', relative_y=44.0)
            with Note(default_x=434.32, default_y=5.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=463.47, default_y=20.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='33', width=522.99):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(51.6)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=111.69, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=137.13, default_y=0.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Attributes():
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=190.65, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=216.08, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=241.52, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=266.95, default_y=-60.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=292.38, default_y=-50.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Attributes():
                with Clef():
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=343.37, default_y=0.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=368.8, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', default_y=1.04, relative_y=44.0)
            with Note(default_x=394.23, default_y=0.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=419.66, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=445.1, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=470.53, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=495.96, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='34', width=388.59):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Attributes():
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=74.3, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=96.57, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=118.85, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=141.12, default_y=0.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=163.39, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=185.66, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=207.93, default_y=-10.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=230.2, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=252.47, default_y=-30.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=274.74, default_y=-20.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=297.01, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=319.28, default_y=-35.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=341.55, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=363.82, default_y=-45.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='35', width=113.98):
            with Direction(placement='above'):
                with DirectionType():
                    Words('C,G,E', relative_y=44.0)
            with Note(default_x=15.8, default_y=-40.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Note(default_x=15.8, default_y=-30.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Note(default_x=15.8, default_y=-15.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=509.66):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-137.0, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=124.22, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=200.99, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-137.0, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=328.94, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=405.7, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=98.27, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=302.99, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='2', width=436.3):
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-87.0, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=42.32, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=120.8, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-87.0, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=251.59, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=330.07, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=225.07, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='3', width=540.44):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('B', default_y=-90.35, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=92.14, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=181.48, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('B', default_y=-90.35, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=330.38, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=419.72, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=62.0, default_y=-185.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=300.24, default_y=-185.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='4', width=485.12):
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-87.0, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=45.37, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=133.0, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-87.0, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=279.05, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=366.68, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=249.48, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='5', width=531.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-87.0, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=91.57, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=179.18, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-87.0, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=325.21, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=412.83, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=62.0, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=295.64, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='6', width=494.31):
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-87.0, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=45.95, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=135.3, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-87.0, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=284.22, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=373.58, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=254.08, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='7', width=531.25):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('B', default_y=-90.35, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=91.57, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=179.18, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('B', default_y=-90.35, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=325.21, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=412.83, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=62.0, default_y=-185.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=295.64, default_y=-185.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='8', width=494.31):
            with Direction(placement='below'):
                with DirectionType():
                    Words('B', default_y=-90.35, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=45.95, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=135.3, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('B', default_y=-90.35, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=284.22, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=373.58, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-185.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=254.08, default_y=-185.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='9', width=525.54):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('A', default_y=-95.75, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=91.21, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=177.76, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('A', default_y=-95.75, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=322.0, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=408.55, default_y=-180.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=62.0, default_y=-190.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=292.79, default_y=-190.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='10', width=500.02):
            with Attributes():
                with Clef(after_barline='yes'):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    Words('D', default_y=-64.1, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', default_y=1.65, relative_y=44.0)
            with Note(default_x=67.52, default_y=-130.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=154.7, default_y=-130.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('D', default_y=-64.1, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', default_y=1.65, relative_y=44.0)
            with Note(default_x=297.92, default_y=-130.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=383.85, default_y=-130.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=38.51, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=268.91, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='11', width=520.08):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-53.25, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', default_y=1.65, relative_y=44.0)
            with Note(default_x=88.78, default_y=-125.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=174.72, default_y=-125.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-53.25, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', default_y=1.65, relative_y=44.0)
            with Note(default_x=317.95, default_y=-125.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=403.89, default_y=-125.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=59.77, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=288.94, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='12', width=505.49):
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-53.25, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B♭', default_y=4.05, relative_y=44.0)
            with Note(default_x=43.73, default_y=-125.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B♭', relative_y=44.0)
            with Note(default_x=135.76, default_y=-125.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-53.25, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B♭', default_y=4.05, relative_y=44.0)
            with Note(default_x=289.15, default_y=-125.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B♭', relative_y=44.0)
            with Note(default_x=381.18, default_y=-125.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.7, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=258.11, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='13', width=528.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('F', default_y=-56.6, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', default_y=1.65, relative_y=44.0)
            with Note(default_x=89.95, default_y=-130.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=177.31, default_y=-130.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('F', default_y=-56.6, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', default_y=1.65, relative_y=44.0)
            with Note(default_x=322.91, default_y=-130.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('A', relative_y=44.0)
            with Note(default_x=410.27, default_y=-130.0, dynamics=141.11):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=60.47, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=293.43, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='14', width=497.22):
            with Direction(placement='below'):
                with DirectionType():
                    Words('F', default_y=-56.6, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G♯', relative_y=44.0)
            with Note(default_x=43.22, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G♯', relative_y=44.0)
            with Note(default_x=133.7, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('F', default_y=-56.6, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G♯', relative_y=44.0)
            with Note(default_x=284.5, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G♯', relative_y=44.0)
            with Note(default_x=374.98, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.7, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=253.98, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='15', width=518.43):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('E', default_y=-60.35, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=89.33, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=174.83, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('E', default_y=-60.35, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=317.33, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=402.83, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=60.47, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=288.47, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='16', width=507.14):
            with Direction(placement='below'):
                with DirectionType():
                    Words('E', default_y=-60.35, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=43.84, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=136.18, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('E', default_y=-60.35, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=290.08, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=382.42, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.7, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=258.94, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='17', width=537.1):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('D', default_y=-64.1, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=90.5, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=179.5, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('D', default_y=-64.1, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=327.83, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=416.83, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=60.47, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=297.8, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='18', width=488.46):
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=42.67, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=131.51, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=279.57, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=368.41, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.7, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=249.6, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='19', width=537.1):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-68.25, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=90.5, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=179.5, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-68.25, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=327.83, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=416.83, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=60.47, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=297.8, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='20', width=488.46):
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-68.25, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=42.67, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=131.51, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-68.25, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=279.57, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('G', relative_y=44.0)
            with Note(default_x=368.41, default_y=-135.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.7, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=249.6, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='21', width=526.3):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('F', default_y=-82.85, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=89.82, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=176.8, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('F', default_y=-82.85, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=321.76, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=408.73, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=60.47, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=292.4, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='22', width=499.26):
            with Direction(placement='below'):
                with DirectionType():
                    Words('F♯', default_y=-82.85, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=47.94, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=137.88, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('F♯', default_y=-82.85, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=287.79, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=377.74, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.59, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=257.45, default_y=-175.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='23', width=543.0):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('G♯', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=101.5, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=189.48, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G♯', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=336.12, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=424.1, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=71.81, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=306.43, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='24', width=482.56):
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=40.27, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=131.9, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=267.96, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('F', relative_y=44.0)
            with Note(default_x=349.6, default_y=-140.0, dynamics=141.11):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.7, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=240.39, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='25', width=536.67):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=90.47, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=179.39, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=327.59, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=416.51, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=60.47, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=297.59, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='26', width=488.9):
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=42.7, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=131.62, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=279.82, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=368.74, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.7, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=249.82, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='27', width=519.24):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=89.38, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=175.03, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=317.79, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=403.44, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=60.47, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=288.87, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='28', width=506.32):
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E♭', relative_y=44.0)
            with Note(default_x=43.73, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E♭', relative_y=44.0)
            with Note(default_x=136.59, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E♭', relative_y=44.0)
            with Note(default_x=289.98, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E♭', relative_y=44.0)
            with Note(default_x=382.01, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.7, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=258.94, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='29', width=536.67):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=90.47, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=179.39, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=327.59, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('E', relative_y=44.0)
            with Note(default_x=416.51, default_y=-145.0, dynamics=141.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=60.47, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=297.59, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='30', width=488.9):
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=42.7, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=131.62, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=279.82, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=368.74, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.7, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=249.82, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='31', width=531.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=90.13, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=178.05, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G', default_y=-79.5, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=324.59, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D', relative_y=44.0)
            with Note(default_x=412.51, default_y=-150.0, dynamics=141.11):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=60.47, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=294.92, default_y=-170.0, dynamics=141.11):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='32', width=494.23):
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-95.75, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=45.32, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=142.78, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-95.75, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=288.55, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=376.01, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-190.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=259.03, default_y=-190.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
        with Measure(number='33', width=522.99):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-78.02, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=86.26, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('C', relative_y=44.0)
            with Note(default_x=190.29, default_y=-155.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=57.51, default_y=-190.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('2')
                Type('whole')
        with Measure(number='34', width=388.59):
            with Direction(placement='below'):
                with DirectionType():
                    Words('C', default_y=-78.02, relative_y=-6.0)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=42.03, default_y=-160.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    Words('B', relative_y=44.0)
            with Note(default_x=118.48, default_y=-160.0, dynamics=141.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.8, default_y=-190.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('2')
                Type('whole')
        with Measure(number='35', width=113.98):
            with Direction(placement='above'):
                with DirectionType():
                    Words('C,C', relative_y=44.0)
            with Note(default_x=15.8, default_y=-190.0, dynamics=141.11):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Note(default_x=15.8, default_y=-155.0, dynamics=141.11):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')