with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Douze Etudes VII')
    with Identification():
        Creator('F. Chopin', type='composer')
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
            Millimeters(6.0)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1979.53)
            PageWidth(1400.4)
            with PageMargins(type='even'):
                LeftMargin(66.6667)
                RightMargin(66.6667)
                TopMargin(66.6667)
                BottomMargin(133.334)
            with PageMargins(type='odd'):
                LeftMargin(66.6667)
                RightMargin(66.6667)
                TopMargin(66.6667)
                BottomMargin(133.334)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Douze Etudes Op.25', default_x=700.199, default_y=1912.86, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('F. Chopin', default_x=1333.73, default_y=1798.07, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('VII', default_x=700.199, default_y=1846.2, justify='center', valign='top', font_size='14')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=1000.64):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    TopSystemDistance(224.79)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Attributes():
                Divisions(480.0)
                with Key():
                    Fifths(4)
                with Time(print_object='no'):
                    Beats('10')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Lento', relative_x=-44.85, relative_y=50.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=72.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.01, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note():
                Rest(measure='yes')
                Duration(4800.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(4800.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=109.61, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=175.13, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(720.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=251.11, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=298.76, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=346.41, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=394.06, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(720.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=470.04, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=517.69, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=547.47, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=577.26, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=607.04, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=636.82, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=666.6, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=696.39, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=726.28, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=756.18, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=785.96, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=815.75, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=845.53, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=875.31, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=905.09, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=934.88, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=964.66, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='2', width=245.67):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('M.M. ', default_x=-46.8, relative_x=-53.21, relative_y=50.0, font_weight='bold', font_size='12')
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-46.8, relative_x=-53.21, relative_y=50.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                with DirectionType():
                    Words('.', default_x=-46.8, relative_x=-53.21, relative_y=50.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=66.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=1.78, relative_x=8.98, relative_y=23.87):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=81.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=81.87, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=111.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=111.93, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=141.99, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=141.99, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=172.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=172.05, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=202.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=202.11, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=33.0, default_y=-145.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Octave(3)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.44, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=172.05, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=220.9, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='3', width=358.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=109.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=276.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=333.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=109.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=109.97, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=143.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=143.06, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=176.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=176.14, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=209.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.22, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=276.01, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=276.01, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=309.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=309.1, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=109.97, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(840.0)
                Voice('5')
                Type('quarter')
                Dot()
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=233.28, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=256.55, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=276.01, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=333.16, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='4', width=318.16):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=96.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=207.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=54.43, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=54.43, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=96.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=96.87, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=153.91, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=153.91, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=207.1, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=207.1, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=263.52, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=263.52, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=96.87, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=123.39, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.91, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.43, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=207.1, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=233.62, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=263.52, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=290.04, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='5', width=327.98):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=97.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(840.0)
                Voice('1')
                Type('quarter')
                Dot()
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=293.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=17.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=57.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=57.38, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=107.43, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.43, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=148.99, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.99, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=218.3, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=218.3, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=268.48, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=268.48, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=17.23, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=148.99, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=174.08, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=199.86, default_y=-160.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(2)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
            with Note(default_x=218.3, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=3)
            with Note(default_x=243.39, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=268.48, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=293.58, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='6', width=241.36):
            with Note(default_x=12.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=84.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=157.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=48.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=84.82, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=84.82, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=121.17, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=121.17, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=157.52, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=157.52, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=193.87, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=193.87, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.12, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=84.82, default_y=-190.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=157.52, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=216.59, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='7', width=372.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(104.71)
            with Note(default_x=113.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=183.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=276.99, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=113.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=113.41, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=148.48, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.48, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=183.54, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.54, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=230.27, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=230.27, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=276.99, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=276.99, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=323.72, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=323.72, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=113.41, default_y=-149.71):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=183.54, default_y=-189.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=212.29, default_y=-169.71):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=248.24, default_y=-154.71):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=276.99, default_y=-149.71):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=305.75, default_y=-139.71):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=341.69, default_y=-144.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='8', width=299.41):
            with Note(default_x=27.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=105.29, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=182.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=221.72, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=27.67, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=54.61, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.48, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=105.29, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=105.29, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=144.1, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=144.1, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=182.91, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=182.91, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=221.72, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=221.72, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-80.0)
                Staff(2)
            with Note(default_x=27.67, default_y=-144.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=105.29, default_y=-174.71):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=182.91, default_y=-169.71):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-20.0)
                Staff(2)
            with Note(default_x=221.72, default_y=-174.71):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=239.36, default_y=-169.71):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=257.0, default_y=-164.71):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=274.64, default_y=-159.71):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='9', width=355.19):
            with Note(default_x=21.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=61.43, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=101.82, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=101.82, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=161.1, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=161.1, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=221.01, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.14, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=221.01, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=294.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=282.74, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=294.6, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=21.03, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=21.03, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=61.43, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=61.43, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=21.03, default_y=-184.71):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-80.0)
                Staff(2)
            with Note(default_x=101.82, default_y=-189.71):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.2, default_y=-184.71):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.1, default_y=-174.71):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.48, default_y=-164.71):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=221.01, default_y=-154.71):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=250.39, default_y=-149.71):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.16, default_y=-139.71):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(3)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=294.6, default_y=-144.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(180.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.43, default_y=-149.71):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-30.0)
                Staff(2)
        with Measure(number='10', width=219.66):
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=61.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=61.41, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=90.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=90.27, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=119.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=119.14, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=148.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=176.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=176.86, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-80.0)
                Staff(2)
            with Note(default_x=13.75, default_y=-159.71):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Octave(3)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=32.19, default_y=-124.71):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=148.0, default_y=-129.71):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=194.89, default_y=-134.71):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='11', width=396.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=109.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=312.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=370.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=109.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=109.97, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=143.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=143.33, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=176.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=176.7, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=210.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=210.06, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=312.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=312.56, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=345.92, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=345.92, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=109.97, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(720.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=210.06, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='stop')
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=241.56, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=261.03, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=284.29, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=312.56, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=370.18, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=312.61):
            with Note(default_x=15.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=200.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=51.62, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.62, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=101.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=101.22, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=150.82, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.82, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=212.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=250.02, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=250.02, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-56.89, relative_x=-23.42, relative_y=-30.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.38)
                Staff(2)
            with Note(default_x=15.8, default_y=-195.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.62, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=76.42, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.22, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.02, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=150.82, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.62, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=200.42, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=225.22, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=250.02, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=269.49, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.85, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='13', width=278.22):
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=178.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=253.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=14.36, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=48.75, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=48.75, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=83.14, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=83.14, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=117.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=117.53, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=178.39, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=178.39, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=212.78, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=212.78, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.36, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(840.0)
                Voice('5')
                Type('quarter')
                Dot()
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=142.54, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=159.95, default_y=-125.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(3)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
            with Note(default_x=178.39, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=3)
            with Note(default_x=237.79, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='14', width=259.43):
            with Note(default_x=21.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=90.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=21.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=21.03, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=55.91, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=55.91, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=90.79, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=90.79, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=125.67, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=125.67, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=169.26, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.26, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=212.86, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=212.86, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=21.03, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=90.79, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=147.47, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=169.26, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=191.06, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.86, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.66, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='15', width=463.15):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=121.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1440.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(1440.0)
            with Note(default_x=122.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=182.81, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=231.54, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=243.4, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=292.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=304.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=352.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=364.6, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=401.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=413.07, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=122.21, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.51, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=182.81, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.11, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dimin.', default_y=-40.0, relative_x=5.71, relative_y=-35.13, font_style='italic', font_size='11')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=243.4, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=273.7, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.0, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.3, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=364.6, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='16', width=403.88):
            with Note(default_x=23.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1440.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=23.87, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=74.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=86.84, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=138.52, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.39, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=201.5, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=213.36, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=264.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=276.34, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=327.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=339.31, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=3.29, relative_y=-30.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=23.87, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=55.35, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.84, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=118.9, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=150.39, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=181.88, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.36, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=244.85, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=276.34, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=307.82, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=339.31, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=370.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='17', width=379.28):
            with Note(default_x=14.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=256.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(360.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=347.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=3.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=14.87, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=63.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=75.33, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=135.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=135.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=196.27, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=196.27, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=244.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=256.74, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=305.34, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=317.21, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.87, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=45.1, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.33, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.57, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.8, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=166.04, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.27, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.51, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=256.74, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=286.97, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.21, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=347.44, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='18', width=359.76):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=118.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=210.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=118.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=118.41, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=164.52, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=164.52, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=210.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=210.62, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=247.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=247.51, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=284.39, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=284.39, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=321.28, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=321.28, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.82)
                Staff(2)
            with Note(default_x=118.41, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.47, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.52, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.57, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=210.62, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(720.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=321.28, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='19', width=320.39):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(1440.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=7.77, relative_y=19.61):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=72.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=72.83, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=125.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=125.42, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=164.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=164.62, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=203.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=203.83, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=260.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=260.86, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.31, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.83, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(180.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.6, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=125.42, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=203.83, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=232.34, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.86, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(180.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.63, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
        with Measure(number='20', width=336.3):
            with Note(default_x=15.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=228.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=62.98, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=62.98, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=110.17, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=110.17, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=169.56, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.56, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=240.4, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=240.4, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=240.4, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=275.72, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=275.72, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=275.72, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.17, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=140.07, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.56, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.05, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=228.54, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=305.21, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='21', width=229.86):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(1440.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=51.21, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=51.21, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=51.21, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=86.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=86.62, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=86.62, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=122.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=122.03, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=122.03, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=157.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=157.44, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=157.44, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=192.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=192.85, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=192.85, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=41.19)
                Staff(2)
        with Measure(number='22', width=435.14):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=134.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=195.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=230.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Tie(type='stop')
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=246.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=262.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=277.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=300.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=316.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=356.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=410.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=134.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=134.71, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=165.03, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.03, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=195.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=195.35, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=228.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=228.84, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=356.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=356.85, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=387.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=387.16, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=134.71, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=195.35, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=356.85, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='23', width=516.59):
            with Note(default_x=29.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=65.13, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=29.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=29.89, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=65.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=65.13, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=131.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=131.43, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=166.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=166.67, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=166.67, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=252.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=252.55, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=252.55, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=350.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=350.3, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=350.3, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=29.89, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=67.11, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=89.21, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=111.31, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(1)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=131.43, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-78.84)
                Staff(2)
            with Note(default_x=166.67, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=185.33, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=215.23, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=233.89, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=252.55, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=271.21, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=301.74, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=320.4, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=350.3, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=365.96, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=400.29, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=423.56, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=446.82, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=482.13, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='24', width=294.58):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=29.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=93.13, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=215.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=29.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=29.89, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=61.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=61.51, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=104.99, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=104.99, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=136.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=136.83, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=215.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=215.2, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=246.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=246.82, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=29.89, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=93.13, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(180.0)
                Voice('5')
                Type('16th')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.16, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=136.83, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=167.36, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Alter(2.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.31, default_y=-170.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=215.2, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-30.0)
                Staff(2)
            with Note(default_x=269.81, default_y=-175.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='25', width=905.63):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(98.83)
            with Note(default_x=128.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=197.85, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=327.62, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=128.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=128.88, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=197.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=197.85, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=315.75, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=327.62, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=327.62, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=384.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=396.58, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=396.58, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=530.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=542.68, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=542.68, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=705.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=717.82, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=717.82, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=128.88, default_y=-183.83):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=223.82, default_y=-188.83):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(1)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=258.08, default_y=-178.83):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(1)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=286.33, default_y=-183.83):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(1)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=327.62, default_y=-188.83):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-78.49)
                Staff(2)
            with Note(default_x=396.58, default_y=-178.83):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=433.11, default_y=-173.83):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=469.63, default_y=-163.83):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=506.15, default_y=-163.83):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=542.68, default_y=-158.83):
                with Pitch():
                    Step('D')
                    Alter(2.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=579.2, default_y=-153.83):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=615.73, default_y=-143.83):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=652.25, default_y=-138.83):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=717.82, default_y=-188.83):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=754.14, default_y=-188.83):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=786.67, default_y=-183.83):
                with Pitch():
                    Step('D')
                    Alter(2.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=816.57, default_y=-178.83):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=847.1, default_y=-168.83):
                with Pitch():
                    Step('G')
                    Alter(2.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=876.99, default_y=-163.83):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='26', width=340.68):
            with Note(default_x=29.89, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=130.02, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=257.61, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=29.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=29.89, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=70.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=70.63, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=118.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=130.02, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=130.02, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=158.89, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=170.76, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=170.76, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=245.74, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=257.61, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=257.61, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=286.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=298.34, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=298.34, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.49, relative_y=-40.0):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=29.89, default_y=-158.83):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(420.0)
                Voice('5')
                Type('eighth')
                Dot()
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=106.76, default_y=-193.83):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=130.02, default_y=-193.83):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=229.92, default_y=-138.83):
                Grace()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=240.89, default_y=-133.83):
                Grace()
                with Pitch():
                    Step('B')
                    Octave(3)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=257.61, default_y=-133.83):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='27', width=1246.31):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-48.81, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=121.65, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-90.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-90.0)
                Staff(1)
            with Note(default_x=519.13, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=519.13, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=121.65, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=320.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=320.89, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=519.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=519.49, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Note(default_x=687.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=687.26, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-85.0)
                Staff(1)
            with Note(default_x=855.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=855.03, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=1047.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=1047.47, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.65, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=149.77, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=177.89, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=206.01, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=234.12, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=262.24, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=292.77, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=320.89, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=349.01, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=377.12, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=407.02, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=435.14, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=463.26, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=491.37, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(34.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(14)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=519.49, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=561.44, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=603.38, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=645.32, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=687.26, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=729.2, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=771.15, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=813.09, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=855.03, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=887.1, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=919.18, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=951.25, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=983.32, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1015.4, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=1047.47, default_y=-180.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=1081.94, default_y=-180.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1114.02, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1148.49, default_y=-185.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1180.56, default_y=-190.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1212.64, default_y=-195.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
        with Measure(number='28', width=1246.31):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(125.61)
            with Direction():
                with DirectionType():
                    Words('ritenuto', default_y=52.64, relative_x=39.17, relative_y=17.62, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=74.07, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-60.0):
                        Fff()
                Staff(1)
                Sound(dynamics=140.0)
            with Note(default_x=144.42, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=144.42, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=54.2, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('50')
                Staff(1)
                Sound(tempo=50.0)
            with Note(default_x=556.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=556.41, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=144.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=144.42, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=336.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=336.97, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=556.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=556.41, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=757.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=757.71, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=894.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=906.23, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=906.23, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=1084.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=1072.25, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=1084.12, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=146.39, default_y=-230.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=165.71, default_y=-235.61):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.03, default_y=-230.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.5, default_y=-225.61):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=235.98, default_y=-220.61):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=263.14, default_y=-215.61):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=284.81, default_y=-210.61):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=304.89, default_y=-205.61):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=326.51, default_y=-200.61):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=349.48, default_y=-195.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=367.06, default_y=-190.61):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=387.13, default_y=-185.61):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=408.75, default_y=-180.61):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=428.82, default_y=-175.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=448.9, default_y=-170.61):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=470.52, default_y=-165.61):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=492.13, default_y=-160.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=516.01, default_y=-155.61):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=541.48, default_y=-150.61):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=566.9, default_y=-145.61):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=589.88, default_y=-140.61):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=615.35, default_y=-135.61):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=634.67, default_y=-140.61):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=653.98, default_y=-145.61):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=673.3, default_y=-150.61):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=692.62, default_y=-155.61):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=708.28, default_y=-160.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=728.36, default_y=-165.61):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=744.02, default_y=-155.61):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=759.69, default_y=-160.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=781.3, default_y=-165.61):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=796.97, default_y=-170.61):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=812.64, default_y=-175.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=828.3, default_y=-180.61):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=843.97, default_y=-185.61):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=859.63, default_y=-190.61):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=875.3, default_y=-195.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=895.37, default_y=-200.61):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=917.58, default_y=-195.61):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=936.7, default_y=-195.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=952.36, default_y=-190.61):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=972.44, default_y=-195.61):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=988.1, default_y=-185.61):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1003.77, default_y=-190.61):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1025.38, default_y=-195.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1047.0, default_y=-200.61):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1062.67, default_y=-190.61):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1078.33, default_y=-195.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1098.33, default_y=-200.61):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1109.52, default_y=-205.61):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1125.19, default_y=-210.61):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1140.85, default_y=-215.61):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1160.17, default_y=-220.61):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1179.49, default_y=-225.61):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1198.8, default_y=-230.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1225.96, default_y=-235.61):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1251.44, default_y=-240.61):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=1276.91, default_y=-245.61):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(25.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(58)
                    NormalNotes(6)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='29', width=330.83):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    TopSystemDistance(90.42)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=15.52, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-65.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=129.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=255.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=286.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=129.77, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=129.77, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=3.29, relative_y=-65.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=161.11, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=192.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=14.02, relative_y=15.3):
                        Pp()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=223.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=129.77, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=-6.71, relative_y=-25.0):
                        Pp()
                Staff(2)
                Sound(dynamics=55.56)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-60.0)
                Staff(2)
            with Note(default_x=255.12, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=306.07, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-4.99)
                Staff(2)
        with Measure(number='30', width=289.31):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=202.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=263.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=59.84, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=59.84, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=107.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.31, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=154.79, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=154.79, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=240.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=240.24, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-105.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.1, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.84, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.57, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.31, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.05, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.79, default_y=-195.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-60.0)
                Staff(2)
            with Note(default_x=202.26, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=263.98, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='31', width=313.08):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=213.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=288.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(1440.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=62.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=62.53, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=62.53, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=112.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=112.71, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=112.71, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=162.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=162.88, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=162.88, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=213.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=213.05, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=247.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=247.55, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=247.55, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-105.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.45, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.53, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.62, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.71, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.79, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.88, default_y=-195.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-60.0)
                Staff(2)
            with Note(default_x=213.05, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=272.64, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='32', width=313.08):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=213.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=288.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=62.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=62.53, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=62.53, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=112.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=112.71, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=112.71, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=162.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=162.88, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=162.88, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=213.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=213.05, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=247.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=247.55, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-105.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.45, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.53, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.62, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.71, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.79, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.88, default_y=-195.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-60.0)
                Staff(2)
            with Note(default_x=213.05, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=272.64, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='33', width=371.04):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(91.44)
            with Note(default_x=109.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=245.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=289.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=324.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=109.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=158.15, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=158.15, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=158.15, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=201.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=201.9, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=201.9, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=245.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=245.65, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=289.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=289.4, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=336.27, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=336.27, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=336.27, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-95.0)
                Staff(2)
            with Note(default_x=109.61, default_y=-126.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.28, default_y=-136.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.15, default_y=-146.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.03, default_y=-141.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-95.0)
                Staff(2)
            with Note(default_x=201.9, default_y=-136.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=223.78, default_y=-161.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.65, default_y=-196.44):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-60.0)
                Staff(2)
            with Note(default_x=289.4, default_y=-116.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=346.28, default_y=-121.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='34', width=298.51):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.0, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-103.94)
                Staff(1)
            with Note(default_x=201.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=273.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(1440.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=59.73, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=59.73, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=107.1, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.1, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=154.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=154.46, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=234.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=234.4, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-95.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-126.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.04, default_y=-141.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.73, default_y=-161.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.41, default_y=-156.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.1, default_y=-151.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.78, default_y=-176.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.46, default_y=-196.44):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=2, default_y=-60.0)
                Staff(2)
            with Note(default_x=201.83, default_y=-116.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=258.08, default_y=-121.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2)
                Staff(2)
        with Measure(number='35', width=298.51):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=201.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=273.75, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=12.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=59.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=59.73, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=59.73, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=107.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.1, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=107.1, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=154.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=154.46, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=154.46, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=201.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=201.83, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=201.83, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=234.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=234.4, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=234.4, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-95.0)
                Staff(2)
            with Note(default_x=12.36, default_y=-126.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.04, default_y=-141.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.73, default_y=-161.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.41, default_y=-156.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.1, default_y=-151.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.78, default_y=-176.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.46, default_y=-196.44):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=201.83, default_y=-116.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=258.08, default_y=-121.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='36', width=278.24):
            with Note(default_x=25.09, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=25.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
            with Note(default_x=25.09, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
            with Note(default_x=25.09, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=3.29, relative_y=-45.0):
                        Ppp()
                Staff(1)
                Sound(dynamics=17.78)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-83.94)
                Staff(1)
            with Note(default_x=68.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=68.18, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=68.18, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=154.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=154.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=154.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=231.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=231.93, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=231.93, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-95.0)
                Staff(2)
            with Note(default_x=25.09, default_y=-126.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.63, default_y=-141.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.18, default_y=-161.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.72, default_y=-156.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=111.27, default_y=-151.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.82, default_y=-176.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.36, default_y=-196.44):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('smorz.', default_y=-40.0, relative_x=-4.01, relative_y=-30.12, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=197.45, default_y=-116.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=253.47, default_y=-121.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=25.86, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('55')
                Offset(-480.0)
                Staff(1)
                Sound(tempo=55.0)
        with Measure(number='37', width=410.11):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(98.16)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=23.31, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('50')
                Staff(1)
                Sound(tempo=50.0)
            with Note(default_x=109.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=109.61, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=109.61, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=16.62, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-46.94, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=357.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Backup():
                Duration(1440.0)
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=357.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=357.04, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-83.89)
                Staff(2)
            with Note(default_x=109.97, default_y=-133.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=135.71, default_y=-148.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.45, default_y=-168.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.18, default_y=-163.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=212.92, default_y=-158.16):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=238.65, default_y=-183.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.39, default_y=-203.16):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', default_y=10.88, relative_y=10.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=40.0)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('16th')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-60.0)
                Staff(2)
            with Note(default_x=315.86, default_y=-133.16):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=382.77, default_y=-138.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('45')
                Offset(-960.0)
                Staff(1)
                Sound(tempo=45.0)
        with Measure(number='38', width=263.32):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=166.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=238.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=50.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=50.78, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=89.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=89.21, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=127.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=127.63, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=166.05, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=166.05, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=204.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=204.48, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.36, default_y=-138.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=89.21, default_y=-143.16):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-60.0)
                Staff(2)
            with Note(default_x=166.05, default_y=-143.16):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=231.53, default_y=-148.16):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Voice('5')
                Type('32nd')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=242.5, default_y=-143.16):
                Grace()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='39', width=285.63):
            with Note(default_x=14.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=82.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=107.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=190.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=258.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=14.0, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=55.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=55.42, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=107.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.98, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=149.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=149.4, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=190.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=190.82, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=232.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=232.25, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.0, default_y=-138.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=107.98, default_y=-153.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=190.82, default_y=-138.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='40', width=287.26):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=101.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=56.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=56.9, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=101.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=101.81, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.0, default_y=-153.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=101.81, default_y=-148.16):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=202.84, default_y=-163.16):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=257.59, default_y=-168.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='41', width=335.07):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note():
                Rest(measure='yes')
                Duration(1440.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-25.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=109.61, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.28, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.94, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.59, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=216.23, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='42', width=276.25):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(1440.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=68.68, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=68.68, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=117.72, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=117.72, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=156.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=156.95, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=196.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=196.18, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=235.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=235.42, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.12, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.78, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.68, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.2, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=117.72, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(720.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=235.42, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='43', width=304.92):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(1440.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=68.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=68.83, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=121.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=121.87, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=158.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=158.33, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=194.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=194.79, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=247.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=247.82, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.32, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.83, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.35, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.87, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=194.79, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=221.3, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.82, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(180.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=280.16, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='44', width=330.07):
            with Note(default_x=15.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=224.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=61.97, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=61.97, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=108.13, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.13, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=166.88, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=166.88, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=236.46, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=236.46, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=236.46, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=270.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=270.76, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=270.76, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('ten.', default_y=-40.0, relative_x=-4.01, relative_y=-23.11, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=108.13, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=138.03, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.88, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.74, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=224.59, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=299.61, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='45', width=425.03):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(116.84)
            with Direction(placement='below'):
                with DirectionType():
                    Words('poco riten.', default_y=-40.0, relative_x=-6.01, relative_y=-68.2, font_style='italic', font_size='12')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=113.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=312.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=400.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(1440.0)
            with Note(default_x=113.41, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=113.41, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=113.41, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=153.64, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=153.64, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=153.64, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=193.87, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=193.87, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=193.87, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=253.65, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=253.65, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=253.65, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=312.16, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=300.3, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=312.16, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=352.72, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=340.86, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=352.72, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=113.41, default_y=-171.84):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-30.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=193.87, default_y=-171.84):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=224.39, default_y=-201.84):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.65, default_y=-191.84):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.91, default_y=-196.84):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=312.16, default_y=-176.84):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=381.98, default_y=-181.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='46', width=234.48):
            with Direction(placement='below'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=-40.0, relative_x=-27.04, relative_y=-55.18):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=72.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=72.51, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=102.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=102.17, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=131.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=131.84, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=161.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=161.51, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=191.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=191.17, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=3.76, relative_x=-9.14, relative_y=32.33):
                        Fz()
                Staff(2)
                Sound(dynamics=91.11)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-65.0)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-206.84):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(2)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.77, default_y=-171.84):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(3)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=42.48, default_y=-136.84):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=161.51, default_y=-141.84):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=209.71, default_y=-146.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='47', width=266.64):
            with Note(default_x=15.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=183.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=240.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=49.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=49.21, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=82.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=82.61, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=116.02, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=116.02, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=183.05, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.05, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=216.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=216.45, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-146.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(840.0)
                Voice('5')
                Type('quarter')
                Dot()
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=140.31, default_y=-141.84):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=163.58, default_y=-146.84):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=183.05, default_y=-151.84):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=240.75, default_y=-156.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='48', width=320.16):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=97.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-51.29, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=208.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=54.81, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=54.81, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=97.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=97.61, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=154.89, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=154.89, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=208.4, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=208.4, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=265.05, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=265.05, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.0, default_y=-156.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=97.61, default_y=-156.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=124.36, default_y=-161.84):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.89, default_y=-166.84):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.65, default_y=-161.84):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=208.4, default_y=-151.84):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=235.15, default_y=-156.84):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.05, default_y=-166.84):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.8, default_y=-176.84):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='49', width=429.27):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(120.81)
            with Note(default_x=121.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=201.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(840.0)
                Voice('1')
                Type('quarter')
                Dot()
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=394.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.65, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=121.65, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=161.55, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=161.55, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=209.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.35, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=250.91, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=250.91, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=320.06, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=320.06, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=369.93, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=369.93, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.65, default_y=-190.81):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=250.91, default_y=-205.81):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=275.84, default_y=-200.81):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-80.25)
                Staff(2)
            with Note(default_x=301.62, default_y=-190.81):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(2)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
            with Note(default_x=320.06, default_y=-195.81):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=3)
            with Note(default_x=345.0, default_y=-200.81):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=369.93, default_y=-185.81):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=394.87, default_y=-180.81):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='50', width=239.8):
            with Note(default_x=12.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=84.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=156.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=48.19, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=84.27, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=84.27, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=120.34, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=120.34, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=156.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=156.41, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=192.48, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=192.48, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-45.25, relative_y=-40.0):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Note(default_x=12.12, default_y=-175.81):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=84.27, default_y=-220.81):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=156.41, default_y=-165.81):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=215.03, default_y=-165.81):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='51', width=276.13):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=86.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=180.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=51.09, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.09, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=86.39, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=86.39, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=133.43, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=133.43, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=180.46, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=180.46, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=227.5, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=227.5, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-165.81):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=67.95, default_y=-240.81):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=86.39, default_y=-205.81):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=115.33, default_y=-185.81):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.52, default_y=-170.81):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=180.46, default_y=-165.81):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=209.41, default_y=-155.81):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=245.59, default_y=-160.81):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='52', width=301.11):
            with Note(default_x=27.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=105.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=183.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=223.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=27.67, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=54.88, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.74, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=105.82, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=105.82, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=144.9, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=144.9, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=183.98, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.98, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=223.06, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=223.06, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=27.67, default_y=-160.81):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=105.82, default_y=-190.81):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=183.98, default_y=-185.81):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=223.06, default_y=-190.81):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=240.82, default_y=-185.81):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=258.58, default_y=-180.81):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=276.34, default_y=-175.81):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
        with Measure(number='53', width=1000.8):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(189.28)
            with Note(default_x=125.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=159.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=194.29, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=194.29, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-202.16)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-202.16)
                Staff(1)
            with Note(default_x=385.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=385.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Note(default_x=590.02, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=590.02, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=590.02, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=601.89, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=790.09, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=790.09, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=801.96, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=125.45, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=125.45, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=159.87, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=159.87, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=125.45, default_y=-269.28):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-133.54)
                Staff(2)
            with Note(default_x=196.26, default_y=-309.28):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(1)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=215.58, default_y=-304.28):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=234.89, default_y=-299.28):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=262.64, default_y=-299.28):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=281.95, default_y=-294.28):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=309.7, default_y=-294.28):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(1)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=329.01, default_y=-289.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=357.47, default_y=-289.28):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(2)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=379.3, default_y=-284.28):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=419.93, default_y=-279.28):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=447.67, default_y=-279.28):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=471.62, default_y=-274.28):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=494.4, default_y=-274.28):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(2)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=513.31, default_y=-269.28):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=533.38, default_y=-264.28):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=555.72, default_y=-264.28):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=577.92, default_y=-259.28):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=622.85, default_y=-259.28):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=645.19, default_y=-254.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=667.97, default_y=-254.28):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=686.88, default_y=-249.28):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=706.95, default_y=-244.28):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=729.29, default_y=-244.28):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=751.63, default_y=-239.28):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=775.18, default_y=-239.28):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=819.27, default_y=-234.28):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=839.35, default_y=-229.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=861.69, default_y=-229.28):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=881.76, default_y=-224.28):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=904.1, default_y=-224.28):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=930.24, default_y=-219.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=958.7, default_y=-219.28):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(4)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=978.01, default_y=-214.28):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(29.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(33)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-13.98)
                Staff(2)
        with Measure(number='54', width=245.51):
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=52.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=52.53, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=88.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=88.9, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=125.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=125.27, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=161.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=161.64, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=198.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=198.01, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Fz()
                Staff(2)
                Sound(dynamics=122.22)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=15.8, default_y=-209.28):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=161.64, default_y=-214.28):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=220.74, default_y=-219.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='55', width=327.61):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(154.14)
                with StaffLayout(number=2):
                    StaffDistance(90.0)
            with Note(default_x=109.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=263.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=302.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=109.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=109.97, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=126.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=126.97, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=143.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=143.98, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=160.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=160.98, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=263.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=263.48, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=287.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=287.18, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=109.97, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(720.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=160.98, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='stop')
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=192.48, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=211.95, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=235.21, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=263.48, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=302.84, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='56', width=214.06):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.81, relative_x=6.58, relative_y=-55.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=37.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=94.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=155.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=26.03, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=37.9, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=54.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.18, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=82.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=94.45, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=115.76, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=127.62, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=155.9, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=155.9, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=184.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=184.18, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=37.9, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=94.45, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=125.22, default_y=-145.0):
                Grace()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=136.18, default_y=-140.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=155.9, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
        with Measure(number='57', width=171.94):
            with Note(default_x=16.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=107.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=147.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=17.23, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=39.88, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=39.88, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=62.52, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=85.17, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.81, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=131.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.51, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=17.23, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=62.52, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=107.81, default_y=-180.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
        with Measure(number='58', width=271.26):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=108.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=55.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=55.2, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=108.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=108.6, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=147.99, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=147.99, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=187.39, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=187.39, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=226.79, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=226.79, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.5, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.2, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=88.9, default_y=-180.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=108.6, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=128.3, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.99, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.69, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=187.39, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.09, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.79, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=246.49, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='59', width=261.44):
            with Note(default_x=13.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(960.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=179.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=236.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=14.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=63.74, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=63.74, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=102.17, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=102.17, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=140.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=140.6, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=179.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=179.03, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=217.46, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=217.46, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.0, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.22, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.74, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.96, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=102.17, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.39, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.6, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.82, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=179.03, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=198.25, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.46, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.68, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='60', width=309.06):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(93.16)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-95.79)
                Staff(1)
            with Note(default_x=113.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=187.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=113.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=113.41, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=150.73, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.73, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=188.05, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=188.05, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=217.9, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=217.9, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=247.75, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=247.75, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=277.61, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=277.61, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=113.41, default_y=-173.16):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.07, default_y=-158.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.73, default_y=-148.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.39, default_y=-158.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=188.05, default_y=-138.16):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(720.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=277.61, default_y=-148.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='61', width=221.26):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-55.0):
                        Pp()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=15.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=143.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=51.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.23, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=86.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=86.66, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=115.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=115.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=143.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=143.35, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=178.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=178.78, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-123.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=33.51, default_y=-138.16):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.23, default_y=-133.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.94, default_y=-148.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=86.66, default_y=-138.16):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=143.35, default_y=-123.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=161.06, default_y=-138.16):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.78, default_y=-133.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.49, default_y=-148.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='62', width=199.82):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=65.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=38.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=38.9, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=65.79, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=65.79, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=104.91, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=104.91, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=144.43, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=144.43, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=171.32, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=171.32, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=12.0, default_y=-138.16):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=65.79, default_y=-133.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=85.35, default_y=-148.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.91, default_y=-138.16):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(180.0)
                Voice('5')
                Type('16th')
                Dot()
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.76, default_y=-158.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=144.43, default_y=-148.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='63', width=266.8):
            with Note(default_x=15.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('riten.', relative_x=6.01, relative_y=19.97, font_style='italic', font_size='12')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=180.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=50.54, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=50.54, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=85.27, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=85.27, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=85.27, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=137.51, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=137.51, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=137.51, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=192.79, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=192.79, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=192.79, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=220.33, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=220.33, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=220.33, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-93.29)
                Staff(2)
            with Note(default_x=15.8, default_y=-148.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=85.27, default_y=-148.16):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=115.8, default_y=-178.16):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.51, default_y=-168.16):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.22, default_y=-173.16):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.93, default_y=-153.16):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=242.04, default_y=-158.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-32.46)
                Staff(2)
        with Measure(number='64', width=249.38):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-30.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=21.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-65.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-65.0)
                Staff(1)
            with Note(default_x=92.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=21.03, default_y=-138.16):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=21.03, default_y=-128.16):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=21.03, default_y=-113.16):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=48.05, default_y=-138.16):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=48.05, default_y=-128.16):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=48.05, default_y=-113.16):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=92.87, default_y=-143.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.87, default_y=-133.16):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=92.87, default_y=-113.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=146.4, default_y=-143.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=146.4, default_y=-133.16):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=146.4, default_y=-113.16):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=193.75, default_y=-143.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=193.75, default_y=-133.16):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=193.75, default_y=-118.16):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=220.76, default_y=-143.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=220.76, default_y=-133.16):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=220.76, default_y=-118.16):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('ten.', default_y=-76.25, relative_x=-4.01, relative_y=-23.11, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=21.03, default_y=-158.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=92.51, default_y=-158.16):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=126.93, default_y=-183.16):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.4, default_y=-173.16):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.28, default_y=-178.16):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=193.75, default_y=-163.16):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='65', width=467.7):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.76)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(111.29)
            with Note(default_x=109.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=229.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=295.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=354.85, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(420.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=442.93, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=109.61, default_y=-166.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=109.61, default_y=-156.29):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=109.61, default_y=-136.29):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=168.33, default_y=-166.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.33, default_y=-156.29):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=168.33, default_y=-136.29):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=229.2, default_y=-166.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=229.2, default_y=-156.29):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=229.2, default_y=-141.29):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=295.59, default_y=-171.29):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=295.59, default_y=-161.29):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=295.59, default_y=-141.29):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=354.85, default_y=-171.29):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=354.85, default_y=-161.29):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=354.85, default_y=-141.29):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=395.22, default_y=-171.29):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=395.22, default_y=-161.29):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=395.22, default_y=-146.29):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=109.61, default_y=-181.29):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=138.97, default_y=-206.29):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.33, default_y=-196.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.69, default_y=-201.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=229.2, default_y=-186.29):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=263.53, default_y=-211.29):
                with Pitch():
                    Step('C')
                    Alter(2.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('double-sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.59, default_y=-201.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=324.95, default_y=-206.29):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=354.85, default_y=-186.29):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=424.58, default_y=-191.29):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=2)
        with Measure(number='66', width=293.95):
            with Direction(placement='above'):
                with DirectionType():
                    Words('riten.', relative_x=6.01, relative_y=19.97, font_style='italic', font_size='12')
                Staff(1)
                Sound(tempo=58.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-95.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-95.0)
                Staff(1)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=55.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=55.97, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=96.14, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=96.14, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=146.36, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=146.36, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=196.57, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=208.44, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=242.13, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=242.13, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-166.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=55.97, default_y=-156.29):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.14, default_y=-156.29):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=146.36, default_y=-156.29):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.57, default_y=-161.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=242.13, default_y=-161.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-211.29):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=96.14, default_y=-211.29):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=121.25, default_y=-206.29):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.36, default_y=-196.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.46, default_y=-201.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=196.57, default_y=-186.29):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=267.24, default_y=-191.29):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='67', width=237.35):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=59.99, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=59.99, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=101.84, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=113.7, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('riten.', relative_x=6.01, relative_y=19.97, font_style='italic', font_size='12')
                Staff(1)
                Sound(tempo=50.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-60.0, relative_x=11.58, relative_y=-35.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=202.27, default_y=-161.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=202.27, default_y=-146.29):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=202.27, default_y=-136.29):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-166.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=59.99, default_y=-156.29):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=101.84, default_y=-161.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-211.29):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.07, default_y=-206.29):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.99, default_y=-196.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.91, default_y=-201.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=101.84, default_y=-186.29):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=202.27, default_y=-191.29):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
        with Measure(number='68', width=131.23):
            with Note(default_x=15.8, default_y=-166.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=15.8, default_y=-141.29):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=91.69, default_y=-166.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=91.69, default_y=-141.29):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-211.29):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=91.69, default_y=-211.29):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=91.69, default_y=-191.29):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='69', width=116.08):
            with Note(default_x=15.8, default_y=-166.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', relative_y=63.75)
            with Note(default_x=15.8, default_y=-141.29):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.8, default_y=-211.29):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(1440.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=15.8, default_y=-191.29):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(1440.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')