with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Apparitions')
    with Identification():
        Creator('Franz Liszt', type='composer')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(5.588)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2045.45)
            PageWidth(1545.45)
            with PageMargins(type='even'):
                LeftMargin(60.0)
                RightMargin(60.0)
                TopMargin(70.9091)
                BottomMargin(143.636)
            with PageMargins(type='odd'):
                LeftMargin(60.0)
                RightMargin(60.0)
                TopMargin(70.9091)
                BottomMargin(143.636)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Apparitions', default_x=772.727, default_y=1974.55, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('No. 2', default_x=772.727, default_y=1902.96, justify='center', valign='top', font_size='18')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Franz Liszt', default_x=1485.45, default_y=1813.71, justify='right', valign='bottom', font_size='12')
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
        with Measure(number='1', width=417.53):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    TopSystemDistance(230.84)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Attributes():
                Divisions(240.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('6')
                    BeatType('8')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Vivamente.', default_x=-38.74, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=130.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_x=5.29, relative_y=-45.07):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(180.0)
                Voice('1')
                Type('eighth')
                Dot()
                Staff(1)
            with Note(default_x=172.15, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=172.15, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=206.24, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=206.24, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=260.78, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(180.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=260.78, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(180.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=327.29, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=327.29, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=361.38, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=361.38, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-105.67)
                Staff(2)
            with Note(default_x=83.51, default_y=-215.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=83.51, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=172.15, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=172.15, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=206.24, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=206.24, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=260.78, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(180.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=260.78, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(180.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=327.29, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=327.29, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=361.38, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=361.38, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=334.92):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(180.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(180.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-89.88)
                Staff(1)
            with Note(default_x=83.86, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=83.86, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=118.75, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=118.75, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=174.56, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=174.56, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=209.45, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(180.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=209.45, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(180.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=277.51, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=277.51, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(180.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(180.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=83.86, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=83.86, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=118.75, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=118.75, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=174.56, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=174.56, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=209.45, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=209.45, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=277.51, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=277.51, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='3', width=280.53):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-44.46, relative_x=9.56, relative_y=-50.42):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=126.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=173.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note():
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=249.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='4', width=371.77):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=94.44)
            with Note(default_x=13.75, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=32.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=189.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=7.57, relative_x=-2.35, relative_y=28.63):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=314.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=4.78, relative_y=-25.12):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=99.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=99.82, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=134.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=134.48, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=189.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=189.94, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=280.05, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=280.05, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=314.72, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=314.72, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=99.82, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=99.82, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=134.48, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=134.48, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=189.94, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=189.94, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=280.05, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=280.05, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=314.72, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=314.72, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=293.12):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(142.93)
                with StaffLayout(number=2):
                    StaffDistance(138.35)
            with Note(default_x=59.89, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=134.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=175.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=250.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=109.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.54, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=225.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=225.36, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=109.54, default_y=-178.35):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.54, default_y=-168.35):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=225.36, default_y=-213.35):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=225.36, default_y=-188.35):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=225.36, default_y=-168.35):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
        with Measure(number='6', width=306.64):
            with Note(default_x=13.75, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=24.72, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=36.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(720.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        StrongAccent(type='up')
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-67.55, relative_x=-12.97, relative_y=-43.05):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=90.46, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=90.46, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=117.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=117.97, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=161.99, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=161.99, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=233.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=233.51, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=261.02, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=261.02, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=90.46, default_y=-213.35):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=90.46, default_y=-193.35):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=90.46, default_y=-178.35):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=117.97, default_y=-213.35):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=117.97, default_y=-193.35):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=117.97, default_y=-178.35):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=161.99, default_y=-213.35):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=161.99, default_y=-193.35):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=161.99, default_y=-178.35):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=233.51, default_y=-213.35):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=233.51, default_y=-193.35):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=233.51, default_y=-178.35):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=261.02, default_y=-213.35):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=261.02, default_y=-193.35):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=261.02, default_y=-178.35):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=255.12):
            with Note(default_x=12.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=120.29, default_y=-198.35):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=161.29, default_y=-193.35):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=227.9, default_y=-188.35):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='8', width=196.73):
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=89.84, default_y=-60.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=126.31, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=126.31, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-228.35):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(4)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=34.24, default_y=-218.35):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(720.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        StrongAccent(type='up')
        with Measure(number='9', width=353.15):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Staff(1)
                Sound(tempo=160.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=92.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=92.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=135.3, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.3, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=160.29, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.12, default_y=-213.35):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
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
            with Note(default_x=42.02, default_y=-208.35):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=42.02, default_y=-198.35):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
            with Note(default_x=67.01, default_y=-188.35):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
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
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=166.84, default_y=-133.35):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(6)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=185.29, default_y=-128.35):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.12, default_y=-213.35):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('6')
                Type('half')
                Staff(2)
        with Measure(number='10', width=338.18):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(142.93)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('130')
                Staff(1)
                Sound(tempo=130.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('1')
                Type('eighth')
                Dot()
                Staff(1)
            with Note(default_x=133.58, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=133.58, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=161.97, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=161.97, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=207.39, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(180.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=207.39, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(180.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=262.77, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=262.77, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=291.16, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=291.16, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-105.67)
                Staff(2)
            with Note(default_x=59.77, default_y=-215.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=59.77, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=133.58, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=133.58, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=161.97, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=161.97, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=207.39, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(180.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=207.39, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(180.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=262.77, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=262.77, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=291.16, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=291.16, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='11', width=279.31):
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(180.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(180.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-89.88)
                Staff(1)
            with Note(default_x=71.94, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=71.94, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=100.72, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=100.72, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=146.76, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=146.76, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=175.53, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(180.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=175.53, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(180.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=231.67, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=231.67, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(180.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(180.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=71.94, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=71.94, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=100.72, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=100.72, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=146.76, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=146.76, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=175.53, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=175.53, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=231.67, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=231.67, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='12', width=224.92):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-44.46, relative_x=9.56, relative_y=-50.42):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=15.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=103.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=140.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note():
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=200.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='13', width=316.16):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=94.44)
            with Note(default_x=13.75, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=32.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=163.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=7.57, relative_x=-2.35, relative_y=28.63):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=268.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=4.78, relative_y=-25.12):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=88.69, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=88.69, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=117.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=117.65, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=163.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=163.98, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=239.27, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=239.27, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=268.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=268.23, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=88.69, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=88.69, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=117.65, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=117.65, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=163.98, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=163.98, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=239.27, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=239.27, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=268.23, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=268.23, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=246.18):
            with Note(default_x=12.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=87.49, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=128.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=203.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=61.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=61.95, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=178.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=178.18, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=61.95, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=61.95, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=178.18, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=178.18, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=178.18, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
        with Measure(number='15', width=325.63):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(-0.0)
                    SystemDistance(142.93)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Note(default_x=58.71, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=69.68, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=81.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(720.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        StrongAccent(type='up')
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-67.55, relative_x=-12.97, relative_y=-43.05):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=130.23, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=130.23, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=155.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=155.07, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=194.83, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=194.83, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=259.43, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=259.43, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=284.27, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=284.27, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=130.23, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=130.23, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=130.23, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.07, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=155.07, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=155.07, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=194.83, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=194.83, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=194.83, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=259.43, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=259.43, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=259.43, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=284.27, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=284.27, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=284.27, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=237.15):
            with Note(default_x=12.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=11.66, relative_y=-33.9):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=15.02, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Staff(1)
                Sound(tempo=100.0)
            with Note(default_x=103.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=202.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=103.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-17.64):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=103.1, default_y=-130.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=103.1, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=208.17):
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=28.68, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=65.87, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=104.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=14.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=104.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=14.0, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=14.0, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=104.31, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=104.31, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='18', width=333.98):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.45, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('130')
                Staff(1)
                Sound(tempo=130.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=54.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=81.04, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.55, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.11, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=299.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=54.53, default_y=-210.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-29.49)
            with Note(default_x=54.53, default_y=-190.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-29.49)
            with Note(default_x=54.53, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-29.49)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='19', width=299.83):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=12.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=136.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=153.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=183.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=209.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=12.0, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=74.44, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=100.73, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=100.73, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=136.88, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=136.88, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=235.79, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=262.08, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='20', width=512.0):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(142.93)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=8.74, relative_y=-46.74):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=59.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=96.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.08, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.13, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=293.79, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=341.79, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=378.44, default_y=40.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=415.1, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=451.75, default_y=45.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        StrongAccent(type='up')
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=149.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=229.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=309.95, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=378.44, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=59.77, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=181.08, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=217.74, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=217.74, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=293.79, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=293.79, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=415.1, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=451.75, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=292.21):
            with Note(default_x=15.8, default_y=45.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-10.26, relative_y=-33.92):
                        P()
                Staff(1)
                Sound(dynamics=42.22)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=61.31)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-227.59)
                Staff(1)
            with Note(default_x=101.08, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=124.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.47, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=195.85, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=219.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=101.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=148.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=195.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=243.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=77.39, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.08, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.08, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=148.47, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=148.47, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=219.54, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=243.23, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='22', width=317.22):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.92, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=118.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-1.0)
                Staff(1)
            with Note(default_x=143.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=249.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=274.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=66.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=118.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=172.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=274.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=92.49, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=118.05, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=118.05, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=172.48, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=172.48, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=249.16, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=274.72, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='23', width=283.32):
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=129.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=144.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=174.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=199.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Backup():
                Duration(720.0)
            with Note(default_x=12.94, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=71.04, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=95.5, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=95.5, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=129.14, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=129.14, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=223.63, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=248.09, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='24', width=514.06):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    TopSystemDistance(99.77)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=8.74, relative_y=-46.74):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=70.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=104.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.1, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=91.69)
                Staff(1)
            with Note(default_x=291.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=339.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=372.73, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=412.12, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=445.82, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=479.14, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=153.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=230.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=307.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=384.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=445.82, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=479.14, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=70.75, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=185.38, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=218.7, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=218.7, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=291.41, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=291.41, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=412.12, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=445.82, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='25', width=282.53):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-10.19, relative_y=-31.92):
                        P()
                Staff(1)
                Sound(dynamics=42.22)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-229.82)
                Staff(1)
            with Note(default_x=95.34, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=118.61, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.88, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.14, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=188.41, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.53, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.64, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=95.34, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=141.88, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=188.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=234.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.12, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=72.23, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=95.34, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=95.34, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=141.88, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.88, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=211.53, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=234.64, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='26', width=283.69):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.61, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1, relative_x=-8.94)
                Staff(1)
            with Note(default_x=99.22, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.03, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.84, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.64, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Note(default_x=186.45, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=208.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=55.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=99.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=142.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=186.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=77.42, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=99.22, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=99.22, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=142.84, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=142.84, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=208.25, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=237.12, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='27', width=324.48):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=24.62, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.94, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=69.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=123.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=123.09, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=146.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=146.39, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=176.29, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=215.69, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=238.99, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=285.6, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=188.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=285.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.12, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=93.19, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.09, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.09, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=176.29, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=262.29, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=262.29, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=285.6, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='28', width=467.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=72.27, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=91.6, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=117.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=151.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.26, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=220.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=220.62, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=254.97, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=294.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=363.09, default_y=45.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=431.8, default_y=40.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=266.84, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=328.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=59.77, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=151.9, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=186.26, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=186.26, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=254.97, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=363.09, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=363.09, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=397.44, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='29', width=521.05):
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=43.76, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=54.73, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=80.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.22, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.07, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=70.59)
                Staff(1)
            with Note(default_x=342.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=390.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=433.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=476.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=182.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=269.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=359.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=445.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.12, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=123.52, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=166.37, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=166.37, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=257.22, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=257.22, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=390.91, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=433.76, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='30', width=415.94):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=59.12, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('180')
                Staff(1)
                Sound(tempo=180.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-240.99)
                Staff(1)
            with Note(default_x=21.03, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=21.03, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=53.81, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.58, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.36, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.36, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=152.14, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.91, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=217.69, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=217.69, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=250.46, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=283.24, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.02, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.02, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=348.79, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.57, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=21.03, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=119.36, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=152.14, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=152.14, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=217.69, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=316.02, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=348.79, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=348.79, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='31', width=450.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Note(default_x=74.55, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=74.55, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=105.65, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.75, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.86, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.86, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=198.96, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.06, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('vivace', default_y=-40.0, relative_x=39.23, relative_y=-48.52, font_style='italic', font_size='12')
                Staff(1)
                Sound(tempo=220.0)
            with Note(default_x=262.12, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=293.23, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=324.33, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=355.43, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=386.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=417.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=42.7)
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='32', width=307.74):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=36.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=61.02, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.54, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Note(default_x=159.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=183.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=232.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=257.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=281.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(720.0)
                Voice('5')
                Staff(2)
        with Measure(number='33', width=289.73):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=35.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=59.61, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=83.41, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.22, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.02, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=154.83, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=178.63, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.43, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.24, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=11.41, relative_y=37.7):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=250.04, default_y=-205.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
        with Measure(number='34', width=93.36):
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(360.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='35', width=123.58):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Adagio', default_y=5.96, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=110.0)
            with Note(default_x=12.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=45.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note():
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=98.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Backup():
                Duration(360.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='36', width=140.01):
            with Note(default_x=13.75, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=26.12)
            with Note(default_x=32.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(720.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Fermata(None, type='upright', relative_y=26.12)
                    with Articulations():
                        StrongAccent(type='up')
            with Backup():
                Duration(720.0)
            with Note():
                Rest(measure='yes')
                Duration(720.0)
                Voice('5')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='37', width=306.71):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=44.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Tempo I.', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=100.0)
            with Note(default_x=71.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(360.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=20.29, relative_y=45.41):
                        BeatUnit('quarter')
                        PerMinute('110')
                Staff(1)
                Sound(tempo=110.0)
            with Note(default_x=174.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=243.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=262.47, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=281.94, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=27.78)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=53.37, default_y=-135.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(4)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=71.81, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=71.81, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=106.05, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=140.29, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=174.53, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=208.77, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=243.01, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='38', width=235.72):
            with Note(default_x=17.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=125.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=161.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=197.97, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=17.23, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=53.38, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.53, default_y=-130.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=125.67, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=161.82, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=197.97, default_y=-130.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='39', width=268.55):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=17.99, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('125')
                Staff(1)
                Sound(tempo=125.0)
            with Note(default_x=54.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=92.22, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-43.29)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=117.99, default_y=5.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=154.47, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=17.23, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=54.73, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.22, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=154.47, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=191.96, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=229.46, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='40', width=298.39):
            with Note(default_x=17.23, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.95, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('110')
                Staff(1)
                Sound(tempo=110.0)
            with Note(default_x=63.82, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=110.42, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=157.01, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=203.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=250.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=17.23, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=63.82, default_y=-130.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=110.42, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=157.01, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=203.61, default_y=-130.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=250.2, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=157.01, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='41', width=295.39):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=43.87)
                Staff(1)
            with Note(default_x=139.22, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=228.94, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=249.78, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.63, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=17.23, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=57.89, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.56, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=149.22, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=148.42, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=188.28, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=228.94, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='42', width=373.98):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(-0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Note(default_x=82.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=236.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=285.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=329.02, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(default_x=82.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=236.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=285.66, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=329.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=92.78, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=246.6, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=91.98, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=149.87, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=193.23, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=245.79, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=285.66, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=329.02, default_y=-130.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='43', width=298.49):
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=49.31, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('125')
                Staff(1)
                Sound(tempo=125.0)
            with Note(default_x=66.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.98, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Rfz()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=149.66, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=107.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=149.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=27.23, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=159.66, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=26.43, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=66.29, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=107.98, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=158.86, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=213.52, default_y=-115.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=255.21, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='44', width=346.83):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=21.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(90.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(4)
                    NormalNotes(3)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=21.03, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(90.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(4)
                    NormalNotes(3)
                Stem('down')
                Staff(1)
            with Note(default_x=60.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(90.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(4)
                    NormalNotes(3)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=60.44, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(90.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(4)
                    NormalNotes(3)
                Stem('down')
                Staff(1)
            with Note(default_x=118.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(90.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(4)
                    NormalNotes(3)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=118.56, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(6)
                Duration(90.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(4)
                    NormalNotes(3)
                Stem('down')
                Staff(1)
            with Note(default_x=170.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(90.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(4)
                    NormalNotes(3)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=170.15, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(90.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(4)
                    NormalNotes(3)
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=49.31, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('110')
                Staff(1)
                Sound(tempo=110.0)
            with Note(default_x=208.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=208.87, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=257.93, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=257.93, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=301.58, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=301.58, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=31.03, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=218.87, default_y=-130.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=30.23, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=86.81, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.31, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=218.06, default_y=-130.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=257.93, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=301.58, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='45', width=385.45):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=21.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=21.03, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=21.03, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=5.41, relative_y=38.65):
                        BeatUnit('quarter')
                        PerMinute('110')
                Staff(1)
                Sound(tempo=110.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=270.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=282.18, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=330.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=330.51, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=21.03, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=82.8, default_y=-190.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=113.01, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.22, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.42, default_y=-165.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.63, default_y=-155.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=233.84, default_y=-150.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=282.18, default_y=-125.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=330.51, default_y=-120.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('140')
                Offset(-660.0)
                Staff(1)
                Sound(tempo=140.0)
        with Measure(number='46', width=442.78):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=74.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=74.55, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=74.55, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.95, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('110')
                Staff(1)
                Sound(tempo=110.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=329.77, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=341.63, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=391.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=391.41, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=74.55, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=136.32, default_y=-190.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.42, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.53, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=229.64, default_y=-165.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.75, default_y=-155.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=291.86, default_y=-150.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=341.63, default_y=-125.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=391.41, default_y=-120.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('140')
                Offset(-660.0)
                Staff(1)
                Sound(tempo=140.0)
        with Measure(number='47', width=574.4):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    with Articulations():
                        Staccato()
            with Note(default_x=17.23, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=15.02, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Staff(1)
                Sound(tempo=120.0)
            with Note(default_x=59.24, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=71.1, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=124.97, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=124.97, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=178.84, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=178.84, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=223.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=223.41, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=267.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=267.98, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=312.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=312.54, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=357.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    with Articulations():
                        Staccato()
            with Note(default_x=357.11, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=399.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=399.67, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=441.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=441.6, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=478.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=478.95, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=518.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=518.48, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-115.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(80.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=71.1, default_y=-150.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(80.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=124.97, default_y=-155.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=178.84, default_y=-160.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=223.41, default_y=-160.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=267.98, default_y=-160.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=312.54, default_y=-165.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=357.11, default_y=-165.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    with Articulations():
                        Staccato()
            with Note(default_x=399.67, default_y=-170.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=441.6, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=478.95, default_y=-175.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=518.48, default_y=-180.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
        with Measure(number='48', width=387.57):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=17.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=17.23, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('110')
                Staff(1)
                Sound(tempo=110.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=279.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=291.6, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=330.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=330.35, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(2)
                Sound(dynamics=61.11)
            with Note(default_x=48.87, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=80.51, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=112.15, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=143.79, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=175.43, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=207.07, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=279.73, default_y=-160.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=330.35, default_y=-155.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Offset(-660.0)
                Staff(1)
                Sound(tempo=160.0)
        with Measure(number='49', width=375.08):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(-0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=70.75, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=70.75, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('110')
                Staff(1)
                Sound(tempo=110.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=284.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=296.45, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=335.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=335.14, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=70.75, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=94.71, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=118.67, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=142.63, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=166.59, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=190.55, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=214.5, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=284.58, default_y=-160.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=335.14, default_y=-155.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Offset(-660.0)
                Staff(1)
                Sound(tempo=160.0)
        with Measure(number='50', width=623.82):
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    with Articulations():
                        Staccato()
            with Note(default_x=17.23, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Staff(1)
                Sound(tempo=120.0)
            with Note(default_x=76.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=88.32, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=135.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=135.69, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=194.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=194.91, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=243.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=243.91, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=292.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=292.91, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=341.91, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=341.91, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=401.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    with Articulations():
                        Staccato()
            with Note(default_x=401.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=453.42, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=453.42, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=496.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=496.76, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=540.09, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=540.09, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=581.15, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=581.15, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-150.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(80.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    with Articulations():
                        Staccato()
            with Note(default_x=76.46, default_y=-185.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=135.69, default_y=-190.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=194.91, default_y=-195.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=243.91, default_y=-195.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=292.91, default_y=-195.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=341.91, default_y=-200.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=401.23, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    with Articulations():
                        Staccato()
            with Note(default_x=453.42, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=496.76, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=540.09, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=581.15, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
        with Measure(number='51', width=262.8):
            with Note(default_x=21.03, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=21.03, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('110')
                Staff(1)
                Sound(tempo=110.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-47.22, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=148.72, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=188.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=224.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Backup():
                Duration(720.0)
            with Note(default_x=21.03, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=1.17, relative_y=-27.82):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Note(default_x=43.83, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=66.64, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=89.44, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=112.24, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Offset(-660.0)
                Staff(1)
                Sound(tempo=160.0)
        with Measure(number='52', width=143.06):
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(360.0)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.83, relative_x=7.94, relative_y=-23.77):
                        Mf()
                Staff(2)
                Sound(dynamics=77.78)
            with Note(default_x=34.1, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=55.15, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.2, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=97.25, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=118.29, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Offset(-300.0)
                Staff(1)
                Sound(tempo=160.0)
        with Measure(number='53', width=441.21):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('110')
                Staff(1)
                Sound(tempo=110.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-41.23, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=71.31, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Note(default_x=113.33, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=155.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('130')
                Staff(1)
                Sound(tempo=130.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.1, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=251.21, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.2)
                Staff(1)
            with Note(default_x=284.85, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=318.49, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.2, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(1)
            with Note(default_x=352.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Note(default_x=385.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(720.0)
            with Note():
                Rest(measure='yes')
                Duration(720.0)
                Voice('5')
                Staff(2)
        with Measure(number='54', width=255.31):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=115.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('110')
                Staff(1)
                Sound(tempo=110.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=200.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest(measure='yes')
                Duration(720.0)
                Voice('5')
                Staff(2)
        with Measure(number='55', width=331.71):
            with Note(default_x=12.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=115.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=171.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=274.21, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=44.44)
            with Note(default_x=80.28, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=239.27, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=80.28, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=80.28, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=239.27, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=239.27, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
        with Measure(number='56', width=376.53):
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=183.41, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=316.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-78.72, relative_x=-13.71, relative_y=-31.88):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=87.65, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=87.65, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=124.48, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=124.48, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=183.41, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=183.41, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=279.17, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=279.17, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=316.0, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=316.0, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=87.65, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=87.65, default_y=-175.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=124.48, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=124.48, default_y=-175.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=183.41, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=183.41, default_y=-175.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('6')
                Type('16th')
                Staff(2)
            with Note(default_x=279.17, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=316.0, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='57', width=401.4):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Note(default_x=59.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=168.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=227.35, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=335.93, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=-4.63, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=131.68, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=131.68, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=299.13, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(2)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Staff(2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=299.13, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=299.13, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
        with Measure(number='58', width=307.61):
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
            with Note(default_x=16.87, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(720.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-48.1, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=78.06, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=78.06, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=109.24, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.24, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=159.12, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=159.12, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=219.95, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=251.13, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=78.06, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=78.06, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=109.24, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.24, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=159.12, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=159.12, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=219.95, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=251.13, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='59', width=274.69):
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('130')
                Staff(1)
                Sound(tempo=130.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-78.41)
                Staff(1)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=58.02, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=110.79, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.82, relative_y=-38.6):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=153.01, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-68.1, relative_x=-15.06, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=84.4, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=110.79, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=153.01, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-76.18, relative_y=-40.0):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Note(default_x=204.49, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=230.87, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=84.4, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=84.4, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=110.79, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=110.79, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=153.01, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=153.01, default_y=-175.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=204.49, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=230.87, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='60', width=246.13):
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=44.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.52, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=108.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=149.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=204.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Staff(1)
            with Note(default_x=174.3, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=174.3, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=204.19, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=204.19, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=174.3, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=174.3, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=204.19, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=204.19, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='61', width=174.92):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=12.0, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=12.0, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='62', width=536.0):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(114.29)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=3.29, relative_y=-49.47):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('130')
                Staff(1)
                Sound(tempo=130.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-213.93)
                Staff(1)
            with Note(default_x=115.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=115.68, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=154.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.31, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=196.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.24, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Note(default_x=234.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=234.87, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                    Tuplet(type='start', bracket='yes')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.71)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-213.93)
                Staff(1)
            with Note(default_x=302.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.1, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=337.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=337.56, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=379.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=379.49, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=408.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.08, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.71, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=450.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccatissimo()
                        Accent()
            with Note(default_x=450.01, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=115.68, default_y=-169.29):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=103.81, default_y=-139.29):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=115.68, default_y=-134.29):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='63', width=178.51):
            with Note():
                Rest(measure='yes')
                Duration(720.0)
                Voice('1')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(720.0)
            with Note():
                Rest(measure='yes')
                Duration(720.0)
                Voice('5')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='64', width=361.12):
            with Attributes():
                with Key():
                    Fifths(3)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=7.94, relative_y=-45.41):
                        Mp()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Maggiore.', default_y=13.2, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=130.0)
            with Note(default_x=44.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=44.95, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=208.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=208.52, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=258.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=258.85, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=309.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=309.19, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=126.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=158.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=208.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=126.74, default_y=-119.29):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=158.19, default_y=-119.29):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=208.52, default_y=-119.29):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=44.95, default_y=-189.29):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('6')
                Type('half')
                Staff(2)
        with Measure(number='65', width=329.13):
            with Note(default_x=16.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=16.18, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=171.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=171.86, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-58.1, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=94.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-60.6, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=249.69, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=279.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=94.02, default_y=-119.29):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.95, default_y=-119.29):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=249.69, default_y=-124.29):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=279.63, default_y=-124.29):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=16.18, default_y=-154.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=171.86, default_y=-154.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='66', width=471.87):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=1.17, relative_y=-35.94):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=99.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=99.73, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=292.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=292.41, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-42.74, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=410.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=410.99, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-56.11, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=196.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=233.13, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-56.76, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=351.7, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=196.07, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=233.13, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-3.0)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=351.7, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=99.73, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='67', width=411.09):
            with Note(default_x=12.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=12.12, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=78.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=78.35, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=144.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=144.57, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=210.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=210.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=277.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=277.03, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=343.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=343.26, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.57, relative_x=6.58, relative_y=-12.94):
                        Pp()
                Staff(2)
                Sound(dynamics=44.44)
            with Note(default_x=78.35, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=78.35, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=78.35, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=144.57, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=144.57, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=144.57, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-3.0)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=277.03, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=277.03, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=288.9, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note():
                Rest(measure='yes')
                Duration(720.0)
                Voice('6')
                Staff(2)
        with Measure(number='68', width=521.8):
            with Note(default_x=14.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
                        Staccatissimo()
            with Note(default_x=14.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=85.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=85.47, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=246.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=246.28, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=290.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=290.95, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=335.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=335.63, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=374.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=386.19, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=430.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=430.86, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=475.53, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=475.53, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=130.14, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=130.14, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=130.14, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=174.81, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=174.81, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=174.81, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='69', width=482.34):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=111.65, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=111.65, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=168.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        StrongAccent(type='up')
            with Note(default_x=168.44, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=239.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=239.41, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=296.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=296.2, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=352.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=352.98, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=423.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=423.96, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.33)
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.86, relative_x=1.17, relative_y=-15.65):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=203.92, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=203.92, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=203.92, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=239.41, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=239.41, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=239.41, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-3.0)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-51.76, relative_y=-40.0):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.33)
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.86, relative_x=1.17, relative_y=-15.65):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=388.47, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=388.47, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=423.96, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=423.96, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-3.0)
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=111.65, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=296.2, default_y=-185.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
        with Measure(number='70', width=496.04):
            with Note(default_x=13.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=13.47, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=46.76)
                Staff(1)
            with Note(default_x=204.91, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=204.91, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=204.91, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=236.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.37, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=267.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=267.83, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=299.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=299.3, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=330.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.76, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=362.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=362.22, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=393.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=393.68, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=418.87, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=418.87, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=444.06, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=444.06, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Note(default_x=469.25, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=469.25, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(30.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.33)
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.86, relative_x=1.17, relative_y=-15.65):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=109.19, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.19, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=149.49, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=149.49, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-3.0)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=5.06, relative_x=1.0, relative_y=40.4):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.33)
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=299.3, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=287.43, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=299.3, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=13.47, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=204.91, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='71', width=426.38):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=13.75, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=32.19, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=32.19, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=236.34, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=236.34, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=299.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=30.51)
            with Note(default_x=299.15, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=30.51)
            with Note(default_x=361.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=361.97, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_x=-22.0, relative_y=-34.59):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.33)
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Note(default_x=134.27, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=134.27, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=134.27, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=173.52, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=173.52, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=173.52, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-3.0)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.33)
                Staff(2)
            with Note(default_x=236.34, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=236.34, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=236.34, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=32.19, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
        with Measure(number='72', width=384.06):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Note(default_x=103.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        StrongAccent(type='up')
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=103.41, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=248.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.32, default_y=25.51)
            with Note(default_x=248.52, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.32, default_y=25.51)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_x=-23.35, relative_y=-38.65):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.33)
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Note(default_x=175.97, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=175.97, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=175.97, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=203.87, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=203.87, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=203.87, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-3.0)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.33)
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=293.17, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=293.17, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=337.81, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=103.41, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=293.17, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
        with Measure(number='73', width=316.74):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=0.49, relative_y=58.94):
                        BeatUnit('quarter')
                        PerMinute('120')
                Staff(1)
                Sound(tempo=120.0)
            with Note(default_x=25.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        StrongAccent(type='up')
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=25.09, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=6.49, relative_x=3.29, relative_y=34.99):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=170.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=170.11, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=3.29, relative_y=39.05):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=266.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=266.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.33)
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=73.43, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.33)
                Staff(2)
            with Note(default_x=170.11, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=73.43, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=170.11, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Note(default_x=88.43, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('7')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=121.77, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=180.11, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=218.45, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('7')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('7')
                Type('eighth')
                Staff(2)
        with Measure(number='74', width=402.35):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.95, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('130')
                Staff(1)
                Sound(tempo=130.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-83.21)
                Staff(1)
            with Note(default_x=25.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=25.09, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=87.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=15.51)
            with Note(default_x=87.7, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=15.51)
            with Note(default_x=150.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=150.31, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=212.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=212.92, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=275.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=275.53, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=338.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=30.51)
            with Note(default_x=338.14, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-69.84, relative_y=-40.0):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.33)
                Staff(2)
            with Note(default_x=25.09, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Note(default_x=87.7, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=75.83, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=87.7, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=150.31, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=138.44, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=150.31, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.33)
                Staff(2)
            with Note(default_x=212.92, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=201.06, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=212.92, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=275.53, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=263.67, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=275.53, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='75', width=301.6):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-48.21, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=25.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=25.09, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=70.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=70.91, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=116.73, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        StrongAccent(type='up')
            with Note(default_x=116.73, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=208.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=208.37, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=254.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=254.18, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.33)
                Staff(2)
            with Note(default_x=25.09, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=10.06, relative_y=-22.41):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Note(default_x=70.91, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=70.91, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=70.91, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=116.73, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=116.73, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=116.73, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=162.55, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=162.55, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=162.55, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='76', width=560.07):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-87.18)
                Staff(1)
            with Note(default_x=135.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=135.05, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=166.68, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.68, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.45, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Staff(1)
                Sound(tempo=120.0)
            with Note(default_x=198.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.31, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=229.94, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=229.94, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=261.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=261.58, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.45, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Staff(1)
                Sound(tempo=100.0)
            with Note(default_x=293.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=293.21, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=316.62, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.62, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=340.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=340.04, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=363.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=363.45, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=386.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=386.87, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=410.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=410.28, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-66.89, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Adagio', default_y=15.28, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=30.0)
            with Note(default_x=449.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=461.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Tenuto()
            with Note(default_x=489.08, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=512.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Tenuto()
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=103.41, default_y=-195.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=166.68, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=154.81, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=166.68, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=229.94, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=218.08, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=229.94, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=293.21, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=281.34, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=293.21, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=449.68, default_y=-155.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Fermata(None, type='upright', relative_y=10.0)
                    with Articulations():
                        Tenuto()
            with Note(default_x=489.08, default_y=-165.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
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
                    with Articulations():
                        Tenuto()
            with Note(default_x=512.49, default_y=-160.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
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
                    with Articulations():
                        Tenuto()
        with Measure(number='77', width=313.18):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', default_y=1.2, relative_x=4.06, relative_y=17.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=130.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=127.24, default_y=-40.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=138.21, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=164.16, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-46.15, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=15.8, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=89.51, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=117.86, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=117.86, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=164.16, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=164.16, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=237.87, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=266.22, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='78', width=531.51):
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=96.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=192.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=270.95, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=61.12)
                Staff(1)
            with Note(default_x=366.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='stop')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=54.26, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=96.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=270.95, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=313.22, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=355.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=403.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=445.38, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=445.38, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=487.64, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=487.64, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=138.79, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=181.06, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=181.06, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=270.95, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=270.95, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=403.11, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=445.38, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='79', width=375.39):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(-0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-13.91, relative_y=-31.46):
                        P()
                Staff(1)
                Sound(dynamics=42.22)
            with Direction(placement='above'):
                with DirectionType():
                    Words('molto delicato', relative_x=9.47, relative_y=110.35, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=70.59)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-245.05)
                Staff(1)
            with Note(default_x=184.78, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=208.41, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=232.04, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=255.66, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=279.29, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.91, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=326.54, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=350.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=184.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=232.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=279.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=326.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=99.73, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=-5.7, relative_y=-40.37):
                        Pp()
                Staff(2)
                Sound(dynamics=27.78)
            with Note(default_x=161.16, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=184.78, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=184.78, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=232.04, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=232.04, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=302.91, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=326.54, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='80', width=290.89):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=102.98, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=3.0)
                Staff(1)
            with Note(default_x=193.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=216.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=57.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=102.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=148.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=193.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=80.24, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=102.98, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=102.98, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=148.48, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=148.48, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=216.71, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=243.38, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='81', width=255.78):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_x=8.04, relative_y=-21.06):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=97.73, default_y=-40.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=119.31, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=145.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-46.18, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=12.94, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=67.39, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=88.34, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=88.34, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=145.26, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=145.26, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=199.72, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=220.66, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='82', width=482.7):
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=84.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=168.99, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=51.65)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.71)
                Staff(1)
            with Note(default_x=241.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=325.99, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='stop')
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=48.46, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=84.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=241.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=278.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=362.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.19, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.19, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=12.18)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-48.83, relative_x=3.29, relative_y=-31.88):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=444.64, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=444.64, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.0, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=121.37, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=157.83, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=157.83, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=241.91, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=241.91, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=362.46, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=408.19, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='83', width=414.09):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    TopSystemDistance(98.96)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-12.36, relative_y=-24.53):
                        P()
                Staff(1)
                Sound(dynamics=42.22)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=90.88)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-258.58)
                Staff(1)
            with Note(default_x=196.35, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=223.19, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=250.03, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.87, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=305.14, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=331.98, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.81, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.65, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=196.35, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=250.03, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=305.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=358.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-46.15, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=33.33)
            with Note(default_x=99.73, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=-5.7, relative_y=-40.37):
                        Pp()
                Staff(2)
                Sound(dynamics=27.78)
            with Note(default_x=169.51, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=196.35, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=196.35, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=250.03, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=250.03, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=331.98, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=358.81, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='84', width=281.46):
            with Note(default_x=17.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=104.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Note(default_x=191.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=213.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.93, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=256.7, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=60.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=104.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=147.85, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=191.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=234.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=17.23, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=82.54, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=104.31, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=104.31, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=147.85, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=147.85, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=213.16, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=234.93, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='85', width=339.94):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=21.5, default_y=-40.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=32.47, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=58.42, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.7, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=143.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=143.08, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=172.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=212.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=239.76, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=294.53, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=184.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=294.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-46.15, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=12.12, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=85.8, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=115.7, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=115.7, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=172.98, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=267.14, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=267.14, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=294.53, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='86', width=369.26):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('140')
                Staff(1)
                Sound(tempo=140.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=22.9, default_y=-40.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=33.86, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=59.81, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=89.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.52, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=149.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=149.32, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=179.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=218.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=278.23, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        StrongAccent(type='up')
            with Note(default_x=337.85, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=191.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=248.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=12.12, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=89.62, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=119.52, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=119.52, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=179.22, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=278.23, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=278.23, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=308.04, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='87', width=487.59):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Staff(1)
                Sound(tempo=160.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=140.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=166.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=272.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=311.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=343.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=391.01, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=71.94)
                Staff(1)
            with Note(default_x=420.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=460.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=210.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=283.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=359.18, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=432.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=99.73, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=166.51, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=194.22, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=194.22, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=272.11, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=272.11, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=391.01, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=420.91, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='88', width=458.58):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.82, relative_x=-4.06, relative_y=61.65):
                        BeatUnit('quarter')
                        PerMinute('180')
                Staff(1)
                Sound(tempo=180.0)
            with Note(default_x=18.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=66.84, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.14, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.54, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=169.67, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=217.67, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.2, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=313.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=361.33, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=389.46, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=428.85, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=35.01, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=114.01, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=185.84, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=257.67, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=329.49, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=401.32, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.17)
                Staff(2)
            with Note(default_x=18.84, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=141.54, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=169.67, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=169.67, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=245.8, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=361.33, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=389.46, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=389.46, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='89', width=458.58):
            with Note(default_x=18.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=66.84, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.14, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.54, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=169.67, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=217.67, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.2, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=313.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=361.33, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=389.46, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=428.85, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(default_x=35.01, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=114.01, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=185.84, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=257.67, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=329.49, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=401.32, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=18.84, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=141.54, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=169.67, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=169.67, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=245.8, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=361.33, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=389.46, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=389.46, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='90', width=481.99):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=-12.18, relative_y=94.11):
                        BeatUnit('quarter')
                        PerMinute('240')
                Staff(1)
                Sound(tempo=240.0)
            with Note(default_x=112.21, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.89, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.57, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.26, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=234.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=265.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=326.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=357.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=388.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=419.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=449.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(720.0)
                Voice('5')
                Staff(2)
        with Measure(number='91', width=363.76):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.19, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.37, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.56, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=132.74, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=162.93, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.12, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.3, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=253.49, default_y=-175.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=283.67, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=1.94, relative_y=-91.41):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Note(default_x=313.86, default_y=-215.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='92', width=301.8):
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.68, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Staff(1)
                Sound(tempo=100.0)
            with Note(default_x=133.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=133.81, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=184.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=184.7, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=267.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=267.4, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=133.81, default_y=-130.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=133.81, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=184.7, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=184.7, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=267.4, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=267.4, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(360.0)
            with Note(default_x=133.81, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=184.7, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
        with Measure(number='93', width=257.22):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=207.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.3, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Note(default_x=15.8, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.3, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
        with Measure(number='94', width=357.09):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.7)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(105.0)
            with Note(default_x=99.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=194.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=236.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=313.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=167.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=167.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(180.0)
                Voice('2')
                Type('eighth')
                Dot()
                Staff(1)
            with Note(default_x=287.43, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(120.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=167.8, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=167.8, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=167.8, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=287.43, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=287.43, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='95', width=234.05):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.01, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=18.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=102.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', default_y=9.65, relative_y=10.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=0.53, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Staff(1)
                Sound(tempo=70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=145.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=145.99, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=189.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=189.22, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=18.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=102.77, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=18.43, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=18.43, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=102.77, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=102.77, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=145.99, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=145.99, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=189.22, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=189.22, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='96', width=251.37):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.01, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=18.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(360.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Fermata(None, type='upright', default_y=9.65, relative_y=10.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-51.76, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=108.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=0.53, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('40')
                Staff(1)
                Sound(tempo=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=157.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=157.41, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=157.41, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=203.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=203.59, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=215.46, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=18.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(360.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=108.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=18.43, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=18.43, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(360.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=108.53, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=108.53, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=157.41, default_y=-190.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=157.41, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=203.59, default_y=-200.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=203.59, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='97', width=125.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.68, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=16.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(720.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(720.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=16.87, default_y=-215.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(720.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=16.87, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(720.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='98', width=436.62):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('160')
                Staff(1)
                Sound(tempo=160.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=12.0, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=31.05, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=50.11, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=69.16, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
            with Note(default_x=88.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=107.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=126.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=145.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=164.84, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=188.1, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=211.37, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=234.63, default_y=45.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=257.9, default_y=55.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(23.0)
                Voice('1')
                Type('64th')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Note(default_x=281.17, default_y=65.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(183.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(21)
                    NormalNotes(32)
                    NormalType('64th')
                Stem('down')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(720.0)
                Voice('5')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')