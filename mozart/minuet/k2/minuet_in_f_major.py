with ScorePartwise(version='3.1'):
    with Identification():
        Rights('Left-hand notes may be played detached.')
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
            Millimeters(7.6)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1562.77)
            PageWidth(1105.57)
            with PageMargins(type='even'):
                LeftMargin(52.6316)
                RightMargin(52.6316)
                TopMargin(52.6316)
                BottomMargin(105.263)
            with PageMargins(type='odd'):
                LeftMargin(52.6316)
                RightMargin(52.6316)
                TopMargin(52.6316)
                BottomMargin(105.263)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Minuet in F Major', default_x=552.784, default_y=1510.14, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('K2', default_x=552.784, default_y=1457.51, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Wolfgang Amadeus Mozart\n', default_x=1052.94, default_y=1410.14, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
        CreditWords('(1756-1791)')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Left-hand notes may be played detached.', default_x=552.784, default_y=105.263, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Left-hand notes may be played detached.', default_x=552.784, default_y=105.263, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Left-hand notes may be played detached.', default_x=552.784, default_y=105.263, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Piano', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(77.9528)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=267.15):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.68)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(189.38)
            with Attributes():
                Divisions(6.0)
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('3')
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
                    with Dynamics(default_y=-45.4):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', default_y=3.11, relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('_', default_y=24.45, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=98.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', default_y=9.21, relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('!', default_y=27.95, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=130.86, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=162.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('!!', default_y=18.74, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=214.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=98.43, default_y=-239.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=214.24, default_y=-229.38):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='2', width=181.07):
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('_', default_y=21.34, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=12.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('!', default_y=18.77, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=44.79, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=76.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('!!', default_y=18.74, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=128.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=12.36, default_y=-224.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=128.16, default_y=-224.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=184.51):
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('_', default_y=21.34, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=16.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', default_y=9.83, relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('!', default_y=28.57, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=48.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('4', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=80.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('!!!', default_y=18.74, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=131.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=15.8, default_y=-219.38):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=131.6, default_y=-254.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='4', width=161.74):
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('!!', default_y=18.74, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('4', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('!!.', default_y=18.74, relative_y=20.0, font_weight='bold', font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=110.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(18.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=12.36, default_y=-239.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=61.62, default_y=-254.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=110.88, default_y=-274.38):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='5', width=184.15):
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-208.99)
                Staff(1)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=47.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=79.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('4', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=131.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-13.0)
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=15.44, default_y=-254.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='6', width=229.21):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.68)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(70.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=81.18, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=109.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('4', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=137.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=182.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=80.82, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
        with Measure(number='7', width=246.64):
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=66.29, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=93.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=120.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
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
            with Note(default_x=147.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=217.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Backup():
                Duration(18.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=12.12, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=93.37, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=174.62, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Offset(-16.0)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Offset(-6.0)
                Staff(1)
        with Measure(number='8', width=161.46):
            with Direction(placement='above'):
                with DirectionType():
                    Words('4', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=15.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=100.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(18.0)
            with Note(default_x=15.8, default_y=-100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=58.29, default_y=-115.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=100.77, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=180.57):
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=17.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', default_y=12.17, relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=48.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=79.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=129.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-49.4):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('4', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=17.59, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=160.75):
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=12.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=40.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=69.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=114.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=12.36, default_y=-115.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='11', width=263.07):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.68)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(70.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=77.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=112.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=148.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=204.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', default_y=0.42, relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=77.38, default_y=-100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=148.18, default_y=-95.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=204.82, default_y=-130.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=168.23):
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=16.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=116.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(18.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=17.23, default_y=-115.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=67.03, default_y=-130.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=116.83, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='13', width=182.68):
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=12.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=45.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=77.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=129.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-53.15):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=12.36, default_y=-125.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='14', width=182.68):
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=12.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=45.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=77.48, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=129.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=12.36, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='15', width=181.96):
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('5', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=44.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=76.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=128.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=12.0, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.75, default_y=-100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=128.56, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='16', width=239.3):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.68)
                        RightMargin(-0.0)
                    TopSystemDistance(60.0)
                with StaffLayout(number=2):
                    StaffDistance(966.03)
            with Direction(placement='above'):
                with DirectionType():
                    Words('2', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=77.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=184.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(18.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=77.74, default_y=-1016.03):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=131.06, default_y=-1031.03):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=184.38, default_y=-1051.03):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='17', width=193.25):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-45.4):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', default_y=6.44, relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(1)
            with Note(default_x=12.72, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=47.13, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=81.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=12.36, default_y=-1006.03):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='18', width=193.25):
            with Note(default_x=12.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=47.13, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=81.54, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=12.36, default_y=-1001.03):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='19', width=196.69):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-978.34)
                Staff(1)
            with Note(default_x=16.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=50.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=84.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=140.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-25.99)
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=15.8, default_y=-996.03):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=140.04, default_y=-1031.03):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='20', width=156.12):
            with Note(default_x=12.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=99.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(18.0)
            with Note(default_x=12.36, default_y=-1026.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='21', width=295.14):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.68)
                        RightMargin(-0.0)
                    TopSystemDistance(60.0)
                with StaffLayout(number=2):
                    StaffDistance(70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-45.4):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=77.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=119.24, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=160.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=227.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('3', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=77.38, default_y=-110.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='22', width=230.12):
            with Note(default_x=12.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=54.22, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=95.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=162.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=12.36, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='23', width=233.56):
            with Note(default_x=16.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=99.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=165.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=15.8, default_y=-100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=165.56, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='24', width=219.8):
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=143.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(18.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('1', relative_y=20.0, font_family='Times New Roman', font_size='10.212')
                Staff(2)
            with Note(default_x=12.36, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.97, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=143.58, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')