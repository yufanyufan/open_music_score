with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('BWV 639')
        WorkTitle('Ich ruf zu dir, Herr Jesu Christ')
    with Identification():
        Creator('Christian Fecteau', type='arranger')
        Creator('Johann Sebastian Bach', type='composer')
        Rights('Public Domain')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(7.056)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1683.67)
            PageWidth(1190.48)
            with PageMargins(type='even'):
                LeftMargin(56.6893)
                RightMargin(56.6893)
                TopMargin(56.6893)
                BottomMargin(113.379)
            with PageMargins(type='odd'):
                LeftMargin(56.6893)
                RightMargin(56.6893)
                TopMargin(56.6893)
                BottomMargin(113.379)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Ich ruf zu dir, Herr Jesu Christ', default_x=595.238, default_y=1626.98, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('BWV 639', default_x=595.238, default_y=1570.3, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach', default_x=1133.79, default_y=1526.98, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Public Domain', default_x=595.238, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Public Domain', default_x=595.238, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Public Domain', default_x=595.238, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Pipe Organ', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Pipe Organ')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(20)
                Volume(66.1417)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=325.8):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    TopSystemDistance(164.74)
                with StaffLayout(number=2):
                    StaffDistance(68.24)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(-4)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                Staves(3)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
                with Clef(number=3):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-38.34, default_y=20.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('30')
                Staff(1)
                Sound(tempo=30.0)
            with Note(default_x=130.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Backup():
                Duration(8.0)
            with Note(default_x=130.72, default_y=-108.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=179.09, default_y=-98.24):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=227.46, default_y=-83.24):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.83, default_y=-88.24):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(8.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-71.91, relative_x=5.36, relative_y=-22.04, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=130.72, default_y=-258.24):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=227.46, default_y=-258.24):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(8.0)
            with Note(default_x=133.48, default_y=-293.24, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=230.23, default_y=-293.24, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='2', width=728.8):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=193.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=371.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=504.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=549.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=682.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-83.24):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=60.26, default_y=-98.24):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=104.72, default_y=-108.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=149.19, default_y=-118.24):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=193.65, default_y=-113.24):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=238.11, default_y=-103.24):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=282.57, default_y=-93.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=327.04, default_y=-98.24):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=371.5, default_y=-118.24):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=415.96, default_y=-108.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=460.42, default_y=-98.24):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=504.89, default_y=-103.24):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=549.35, default_y=-108.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=593.81, default_y=-118.24):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=638.27, default_y=-108.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=682.73, default_y=-98.24):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(32.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=2.41, relative_x=5.36, relative_y=9.19, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=15.8, default_y=-223.24):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=104.72, default_y=-223.24):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=193.65, default_y=-223.24):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-40.83, relative_x=4.29, relative_y=-23.11, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=282.57, default_y=-228.24):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=1.8, relative_x=5.51, relative_y=9.8, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=371.5, default_y=-223.24):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=460.42, default_y=-223.24):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue663', default_y=1.98, relative_x=6.13, relative_y=10.42, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=549.35, default_y=-223.24):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', relative_x=6.74, relative_y=12.25, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=638.27, default_y=-228.24):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=22.86, default_y=-258.24, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=111.79, default_y=-258.24, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=200.71, default_y=-258.24, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=289.64, default_y=-263.24, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=378.56, default_y=-258.24, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=467.49, default_y=-258.24, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=556.41, default_y=-258.24, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=645.34, default_y=-263.24, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('flat')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='3', width=594.61):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(104.08)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=137.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=165.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=193.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=221.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=249.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=333.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=351.34, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=368.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=25.0)
            with Note(default_x=480.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=564.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Backup():
                Duration(32.0)
            with Attributes():
                with Clef(number=2, after_barline='yes'):
                    Sign('G')
                    Line(2)
            with Note(default_x=137.54, default_y=-179.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=165.7, default_y=-184.08):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=193.72, default_y=-179.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=221.74, default_y=-169.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=249.76, default_y=-174.08):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=277.79, default_y=-179.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.81, default_y=-184.08):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=333.83, default_y=-179.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=368.85, default_y=-184.08):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=396.87, default_y=-194.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=424.89, default_y=-209.08):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=452.91, default_y=-199.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=480.93, default_y=-204.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=508.95, default_y=-194.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=536.97, default_y=-179.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=564.99, default_y=-169.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(32.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-40.0, relative_x=2.45, relative_y=-23.72, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=137.54, default_y=-269.08):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=193.72, default_y=-269.08):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=249.76, default_y=-269.08):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=305.81, default_y=-269.08):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=368.85, default_y=-274.08):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=424.89, default_y=-274.08):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=4.25, relative_x=6.74, relative_y=7.35, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=480.93, default_y=-259.08):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-40.0, relative_x=4.9, relative_y=-22.5, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=536.97, default_y=-259.08):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=144.6, default_y=-304.08, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=200.79, default_y=-304.08, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=256.83, default_y=-304.08, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=312.87, default_y=-304.08, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=375.92, default_y=-309.08, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=431.96, default_y=-309.08, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=488.0, default_y=-294.08, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=544.04, default_y=-294.08, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='4', width=459.98):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=104.67, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=124.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=209.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=236.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=346.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=400.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(24.0)
            with Note(default_x=124.63, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th', size='cue')
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=153.81, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('2')
                Type('eighth', size='cue')
                Stem('none')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(14.0)
            with Note(default_x=15.8, default_y=-174.08):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=43.01, default_y=-184.08):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=70.21, default_y=-169.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.42, default_y=-174.08):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=124.63, default_y=-169.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=151.83, default_y=-184.08):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=179.04, default_y=-179.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=209.41, default_y=-174.08):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=236.61, default_y=-179.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=263.82, default_y=-189.08):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=291.03, default_y=-179.08):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=318.23, default_y=-169.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=346.4, default_y=-174.08):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=373.6, default_y=-189.08):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=400.81, default_y=-194.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=431.18, default_y=-174.08):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(32.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', relative_x=7.35, relative_y=26.96, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=15.8, default_y=-239.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=70.21, default_y=-239.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=124.63, default_y=-239.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=179.04, default_y=-239.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=236.61, default_y=-239.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=291.03, default_y=-239.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=346.4, default_y=-244.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue663', default_y=0.26, relative_x=7.35, relative_y=17.16, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=400.81, default_y=-249.08):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=22.86, default_y=-274.08, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=77.28, default_y=-274.08, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=131.69, default_y=-274.08, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=186.1, default_y=-274.08, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=243.68, default_y=-274.08, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=298.09, default_y=-274.08, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=353.46, default_y=-279.08, print_object='no'):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=407.88, default_y=-284.08, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='5', width=515.86):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(103.15)
                with StaffLayout(number=3):
                    StaffDistance(73.88)
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=42.92)
            with Note(default_x=107.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('2')
            with Note(default_x=234.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=265.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=285.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=305.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=336.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=368.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(24.0)
            with Note(default_x=107.38, default_y=-178.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=139.04, default_y=-198.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=170.69, default_y=-188.15):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=202.35, default_y=-178.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=234.01, default_y=-163.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=265.67, default_y=-168.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=305.24, default_y=-173.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=336.9, default_y=-168.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=368.56, default_y=-173.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=400.22, default_y=-193.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=431.88, default_y=-183.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=463.53, default_y=-198.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Backup():
                Duration(24.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', relative_x=6.13, relative_y=22.67, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=107.38, default_y=-252.03):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=170.69, default_y=-257.03):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=234.01, default_y=-262.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=305.24, default_y=-267.03):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=368.56, default_y=-272.03):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=431.88, default_y=-282.03):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=114.44, default_y=-287.03, print_object='no'):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=177.76, default_y=-292.03, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=241.08, default_y=-297.03, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=312.31, default_y=-302.03, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=375.62, default_y=-307.03, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=438.94, default_y=-317.03, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='6', width=538.74):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=43.74)
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=141.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=173.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=193.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=213.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=246.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=278.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=407.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-178.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=44.32, default_y=-198.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=76.63, default_y=-188.15):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=108.95, default_y=-178.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=141.26, default_y=-163.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=173.58, default_y=-168.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=213.98, default_y=-173.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=246.29, default_y=-168.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=278.61, default_y=-173.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=310.93, default_y=-198.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=343.24, default_y=-203.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=375.56, default_y=-178.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=407.87, default_y=-208.15):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=440.19, default_y=-188.15):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=472.51, default_y=-203.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=504.82, default_y=-193.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(32.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=0.39, relative_x=6.23, relative_y=21.23, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=12.0, default_y=-252.03):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=76.63, default_y=-257.03):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=141.26, default_y=-262.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=213.98, default_y=-267.03):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-40.0, relative_x=1.23, relative_y=-27.71, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=278.61, default_y=-272.03):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=3.63, relative_x=7.35, relative_y=7.97, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=343.24, default_y=-267.03):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-41.2, relative_x=3.06, relative_y=-30.0, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=407.87, default_y=-282.03):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=472.51, default_y=-282.03):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=19.06, default_y=-287.03, print_object='no'):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=83.7, default_y=-292.03, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=148.33, default_y=-297.03, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=221.04, default_y=-302.03, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=285.67, default_y=-307.03, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=350.31, default_y=-302.03, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=414.94, default_y=-317.03, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=479.57, default_y=-317.03, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='7', width=566.38):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(127.39)
                with StaffLayout(number=3):
                    StaffDistance(73.55)
            with Note(default_x=111.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=222.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=278.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    with Ornaments():
                        InvertedMordent()
            with Note(default_x=296.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=313.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=341.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=397.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=453.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=508.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=111.18, default_y=-227.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=139.09, default_y=-217.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.01, default_y=-222.39):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.92, default_y=-212.39):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=222.83, default_y=-222.39):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=250.75, default_y=-212.39):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.66, default_y=-192.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.55, default_y=-197.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=341.47, default_y=-192.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=369.38, default_y=-207.39):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=397.3, default_y=-212.39):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=425.21, default_y=-197.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=453.12, default_y=-217.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=481.04, default_y=-202.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=508.95, default_y=-192.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=536.87, default_y=-197.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(32.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-40.0, relative_x=1.84, relative_y=-25.56, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=111.18, default_y=-300.94):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=167.01, default_y=-300.94):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-40.0, relative_x=2.45, relative_y=-26.17, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=222.83, default_y=-295.94):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=278.66, default_y=-295.94):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', relative_x=4.9, relative_y=17.16, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=341.47, default_y=-280.94):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-42.06, relative_x=3.68, relative_y=-21.89, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=397.3, default_y=-295.94):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=3.02, relative_x=5.51, relative_y=8.58, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=453.12, default_y=-290.94):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-43.38, relative_x=4.29, relative_y=-25.56, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=508.95, default_y=-300.94):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=118.24, default_y=-335.94, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=174.07, default_y=-335.94, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=229.9, default_y=-330.94, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=285.73, default_y=-330.94, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=348.53, default_y=-315.94, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=404.36, default_y=-330.94, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=460.19, default_y=-325.94, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=516.02, default_y=-335.94, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='8', width=488.22):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=131.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=249.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
            with Note(default_x=368.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=12.0, default_y=-192.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=41.62, default_y=-207.39):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=71.23, default_y=-227.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.6, default_y=-197.39):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=131.22, default_y=-202.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=160.83, default_y=-227.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=190.45, default_y=-232.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.07, default_y=-212.39):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=249.68, default_y=-217.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=279.3, default_y=-227.39):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=308.92, default_y=-217.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=338.53, default_y=-207.39):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=368.15, default_y=-197.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=397.77, default_y=-217.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=427.38, default_y=-222.39):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=457.0, default_y=-197.39):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(32.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=6.09, relative_x=6.13, relative_y=5.51, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=12.0, default_y=-295.94):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-44.71, relative_x=3.68, relative_y=-29.24, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=71.23, default_y=-305.94):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-40.0, relative_x=3.06, relative_y=-28.63, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=131.22, default_y=-300.94):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=6.7, relative_x=5.51, relative_y=4.9, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=190.45, default_y=-295.94):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-70.02, relative_x=6.74, relative_y=-13.92, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=249.68, default_y=-315.94):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=308.92, default_y=-315.94):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=368.15, default_y=-330.94):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=427.38, default_y=-330.94):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=19.06, default_y=-330.94, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=78.3, default_y=-340.94, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=138.28, default_y=-335.94, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=197.51, default_y=-330.94, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=252.45, default_y=-350.94, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=311.68, default_y=-350.94, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=370.91, default_y=-365.94, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=430.15, default_y=-365.94, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='9', width=570.97):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(161.48)
                with StaffLayout(number=2):
                    StaffDistance(97.89)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=119.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=231.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=343.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=457.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=119.98, default_y=-197.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=147.9, default_y=-187.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=175.81, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=203.73, default_y=-167.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=231.9, default_y=-162.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=259.82, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=287.74, default_y=-177.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=315.65, default_y=-162.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=343.57, default_y=-182.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=371.49, default_y=-167.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=401.86, default_y=-162.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=429.77, default_y=-167.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=457.69, default_y=-187.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=485.61, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=513.53, default_y=-167.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=541.45, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(32.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-69.61, relative_x=6.13, relative_y=-24.34, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=119.98, default_y=-287.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=175.81, default_y=-287.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', relative_x=13.02, relative_y=36.0, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=231.9, default_y=-252.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=287.74, default_y=-252.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=1.64, relative_x=8.43, relative_y=9.96, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=343.57, default_y=-252.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-40.0, relative_x=2.3, relative_y=-24.34, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=401.86, default_y=-257.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=1.64, relative_x=8.43, relative_y=9.96, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=457.69, default_y=-252.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-41.84, relative_x=2.3, relative_y=-24.34, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=513.53, default_y=-262.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=122.74, default_y=-322.89, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=178.58, default_y=-322.89, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=234.66, default_y=-287.89, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=290.5, default_y=-287.89, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=350.64, default_y=-287.89, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=408.92, default_y=-292.89, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=464.76, default_y=-287.89, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=520.59, default_y=-297.89, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='10', width=483.63):
            with Note(default_x=12.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=247.17, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=81.1, relative_y=10.0)
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(32.0)
            with Note(default_x=13.04, default_y=-182.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=42.35, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=71.66, default_y=-167.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=100.97, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=130.28, default_y=-177.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=159.6, default_y=-192.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=188.91, default_y=-182.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=218.22, default_y=-187.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=247.53, default_y=-197.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=276.85, default_y=-187.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=306.16, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=335.47, default_y=-177.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=364.78, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=394.09, default_y=-187.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=423.41, default_y=-197.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=452.72, default_y=-207.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('5')
            with Backup():
                Duration(32.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-67.63, relative_x=6.89, relative_y=-11.32, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=13.04, default_y=-272.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=71.66, default_y=-282.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', relative_x=12.25, relative_y=15.32, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=130.28, default_y=-267.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-71.05, relative_x=7.66, relative_y=-2.89, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=188.91, default_y=-267.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-42.33, relative_x=2.3, relative_y=-21.27, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=247.53, default_y=-262.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=306.16, default_y=-262.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=364.78, default_y=-262.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=423.41, default_y=-262.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=15.8, default_y=-307.89, print_object='no'):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=74.42, default_y=-317.89, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=133.05, default_y=-302.89, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=191.67, default_y=-302.89, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=254.6, default_y=-297.89, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=313.22, default_y=-297.89, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=371.85, default_y=-297.89, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=430.47, default_y=-297.89, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='11', width=565.47):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(92.89)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=116.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=226.45, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=336.37, default_y=-35.0):
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
            with Note(default_x=116.18, default_y=-187.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=143.75, default_y=-167.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=171.32, default_y=-162.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=198.88, default_y=-167.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=226.45, default_y=-187.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=254.02, default_y=-172.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=281.59, default_y=-167.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=309.16, default_y=-172.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=336.73, default_y=-182.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=364.3, default_y=-172.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=391.86, default_y=-167.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=419.43, default_y=-172.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=447.6, default_y=-177.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=475.17, default_y=-197.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=508.73, default_y=-187.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=536.3, default_y=-177.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(32.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-44.61, relative_x=6.13, relative_y=-24.34, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=116.18, default_y=-257.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=171.32, default_y=-257.89):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=7.0, relative_x=8.43, relative_y=4.6, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=226.45, default_y=-252.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=281.59, default_y=-252.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-70.33, relative_x=6.89, relative_y=-13.61, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=336.73, default_y=-272.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=391.86, default_y=-272.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-70.69, relative_x=7.66, relative_y=-8.25, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=447.6, default_y=-267.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=508.73, default_y=-267.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=123.24, default_y=-292.89, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=178.38, default_y=-292.89, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=233.52, default_y=-287.89, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=288.65, default_y=-287.89, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=339.49, default_y=-307.89, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=394.63, default_y=-307.89, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=450.36, default_y=-302.89, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=511.5, default_y=-302.89, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='12', width=489.13):
            with Note(default_x=36.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=374.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Attributes():
                with Clef(number=2, after_barline='yes'):
                    Sign('F')
                    Line(4)
            with Note(default_x=36.42, default_y=-137.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=64.61, default_y=-122.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=92.81, default_y=-112.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=121.0, default_y=-117.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=149.2, default_y=-137.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=177.39, default_y=-127.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.58, default_y=-117.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=233.78, default_y=-122.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=261.97, default_y=-147.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=290.17, default_y=-132.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=318.36, default_y=-122.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=346.56, default_y=-127.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=374.75, default_y=-117.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=402.95, default_y=-127.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=431.14, default_y=-147.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=459.33, default_y=-117.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(32.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=0.8, relative_x=12.25, relative_y=15.32, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=36.42, default_y=-262.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=92.81, default_y=-262.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-70.69, relative_x=6.89, relative_y=-8.25, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=149.2, default_y=-267.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=205.58, default_y=-267.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=261.97, default_y=-272.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=318.36, default_y=-272.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=374.75, default_y=-277.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=431.14, default_y=-277.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=39.18, default_y=-297.89, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=95.57, default_y=-297.89, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=151.96, default_y=-302.89, print_object='no'):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=208.35, default_y=-302.89, print_object='no'):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=264.74, default_y=-307.89, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=321.13, default_y=-307.89, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=377.52, default_y=-312.89, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=433.9, default_y=-312.89, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='13', width=528.17):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(0.0)
                    TopSystemDistance(86.0)
                with StaffLayout(number=2):
                    StaffDistance(112.89)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=108.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=212.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=317.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=422.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Note(default_x=108.41, default_y=-162.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=134.55, default_y=-152.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=160.68, default_y=-137.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=186.82, default_y=-142.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=212.95, default_y=-162.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=239.09, default_y=-152.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=265.22, default_y=-142.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=291.36, default_y=-147.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=317.49, default_y=-162.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=343.63, default_y=-152.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=369.76, default_y=-147.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=395.89, default_y=-152.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=422.03, default_y=-157.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=448.16, default_y=-147.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=474.3, default_y=-137.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=500.43, default_y=-142.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(32.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-73.44, relative_x=6.13, relative_y=-20.51, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=108.41, default_y=-302.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue663', default_y=-74.7, relative_x=7.66, relative_y=-20.05, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=160.68, default_y=-302.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-73.08, relative_x=6.89, relative_y=-25.87, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=212.95, default_y=-307.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=265.22, default_y=-307.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=317.49, default_y=-312.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=369.76, default_y=-312.89):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=422.03, default_y=-307.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=474.3, default_y=-307.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=111.18, default_y=-337.89, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=163.45, default_y=-337.89, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=215.72, default_y=-342.89, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=267.99, default_y=-342.89, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=320.26, default_y=-347.89, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=372.52, default_y=-347.89, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=424.79, default_y=-342.89, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=477.06, default_y=-342.89, print_object='no'):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='14', width=526.43):
            with Note(default_x=38.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=66.13, relative_y=4.64)
                    with Technical():
                        Fingering('4')
            with Note(default_x=400.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(32.0)
            with Attributes():
                with Clef(number=2, after_barline='yes'):
                    Sign('G')
                    Line(2)
            with Note(default_x=38.96, default_y=-212.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=68.91, default_y=-202.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=98.86, default_y=-192.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.82, default_y=-177.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=158.77, default_y=-192.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=188.72, default_y=-172.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=218.67, default_y=-167.89):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=248.62, default_y=-172.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=278.57, default_y=-177.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=308.53, default_y=-192.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=338.89, default_y=-182.89):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=370.86, default_y=-212.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=400.81, default_y=-207.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=430.76, default_y=-182.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=464.93, default_y=-212.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=494.88, default_y=-187.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(32.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=4.71, relative_x=8.43, relative_y=6.89, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=38.96, default_y=-292.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=98.86, default_y=-292.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-73.03, relative_x=7.66, relative_y=-15.91, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=158.77, default_y=-297.89):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=218.67, default_y=-297.89):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=278.57, default_y=-302.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=338.89, default_y=-302.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=1.41, relative_x=9.19, relative_y=10.72, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=400.81, default_y=-287.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=464.93, default_y=-287.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=41.72, default_y=-327.89, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=101.63, default_y=-327.89, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=161.53, default_y=-332.89, print_object='no'):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('flat')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=221.44, default_y=-332.89, print_object='no'):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=281.34, default_y=-337.89, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=341.66, default_y=-337.89, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=403.57, default_y=-322.89, print_object='no'):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=467.69, default_y=-322.89, print_object='no'):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='15', width=639.52):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(22.5)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(97.89)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=111.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=242.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=374.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=30.29, relative_x=10.13, relative_y=40.0):
                        BeatUnit('quarter')
                        PerMinute('27')
                Staff(1)
                Sound(tempo=27.0)
            with Note(default_x=506.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=604.99, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(32.0)
            with Note(default_x=111.18, default_y=-202.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=144.1, default_y=-177.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=177.02, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=209.94, default_y=-177.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=242.86, default_y=-207.89):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=275.78, default_y=-182.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=308.7, default_y=-177.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=341.63, default_y=-182.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=374.55, default_y=-212.89):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=407.47, default_y=-187.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=440.39, default_y=-182.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=473.31, default_y=-187.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=506.23, default_y=-192.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=539.15, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=572.07, default_y=-167.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=604.99, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(32.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=3.15, relative_x=8.43, relative_y=13.02, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=111.18, default_y=-272.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-71.1, relative_x=6.89, relative_y=-12.85, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=177.02, default_y=-277.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=242.86, default_y=-277.89):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=308.7, default_y=-282.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=374.55, default_y=-282.89):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=440.39, default_y=-287.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', default_y=1.65, relative_x=12.25, relative_y=20.68, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=506.23, default_y=-262.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=572.07, default_y=-262.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Backup():
                Duration(32.0)
            with Note(default_x=113.94, default_y=-307.89, print_object='no'):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=179.79, default_y=-312.89, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=245.63, default_y=-312.89, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=311.47, default_y=-317.89, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=377.31, default_y=-317.89, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=443.15, default_y=-322.89, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=509.0, default_y=-297.89, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=574.84, default_y=-297.89, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
        with Measure(number='16', width=415.08):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=1.69, relative_y=41.69):
                        BeatUnit('quarter')
                        PerMinute('24')
                Staff(1)
                Sound(tempo=24.0)
            with Note(default_x=14.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=6.76, relative_y=40.0):
                        BeatUnit('quarter')
                        PerMinute('21')
                Staff(1)
                Sound(tempo=21.0)
            with Note(default_x=147.82, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=1.06, relative_y=45.22):
                        BeatUnit('quarter')
                        PerMinute('18')
                Staff(1)
                Sound(tempo=18.0)
            with Note(default_x=281.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(24.0)
            with Note(default_x=14.0, default_y=-182.89):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=47.45, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=80.91, default_y=-167.89):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=114.36, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=147.82, default_y=-177.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=181.27, default_y=-182.89):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=214.73, default_y=-192.89):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=248.18, default_y=-202.89):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=281.75, default_y=-197.89):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=315.2, default_y=-187.89):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=348.66, default_y=-172.89):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Backup():
                Duration(24.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-69.16, relative_x=6.89, relative_y=-9.78, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=14.0, default_y=-272.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=80.91, default_y=-272.89):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue665', relative_x=11.49, relative_y=15.32, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=147.82, default_y=-267.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=214.73, default_y=-267.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('\ue665', default_y=-73.44, relative_x=6.13, relative_y=-20.51, font_family='MScore Text', font_size='16')
                Staff(3)
            with Note(default_x=281.75, default_y=-287.89):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Backup():
                Duration(24.0)
            with Note(default_x=16.76, default_y=-307.89, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Accidental('natural')
                Stem('none')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=83.67, default_y=-307.89, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=150.58, default_y=-302.89, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('continue', number=1)
            with Note(default_x=217.49, default_y=-302.89, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('10')
                Type('eighth', size='cue')
                Stem('none')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=284.51, default_y=-322.89, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('10')
                Type('quarter', size='cue')
                Stem('none')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-heavy')