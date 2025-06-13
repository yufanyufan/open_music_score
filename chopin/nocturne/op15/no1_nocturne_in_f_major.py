with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Nocturne')
    with Identification():
        Creator('Chopin', type='composer')
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
        CreditWords('Nocturne', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Op. 15 No. 1 ', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Chopin', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
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
        with Measure(number='0', implicit='yes', width=148.7):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(65.35)
            with Attributes():
                Divisions(480.0)
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
            with Direction(placement='above'):
                with DirectionType():
                    Words('Antante cantabile ', default_x=-36.94, relative_y=20.0, font_weight='bold', font_size='12')
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.94, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=102.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='1', width=317.81):
            with Note(default_x=13.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=215.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-80.35):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=114.6, default_y=-80.35):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=215.4, default_y=-85.35):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.44, default_y=-115.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-105.35):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=47.4, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.0, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=114.6, default_y=-105.35):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=148.2, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=181.8, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=215.4, default_y=-105.35):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=249.01, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=282.61, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='2', width=274.11):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=100.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=186.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-90.35):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=100.04, default_y=-85.35):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=186.27, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.44, default_y=-115.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-105.35):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=42.55, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=71.29, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=100.04, default_y=-110.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=128.78, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=157.53, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=186.27, default_y=-110.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=215.02, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=243.76, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='3', width=315.87):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=107.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=134.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=224.25, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-90.35):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=134.23, default_y=-85.35):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=224.25, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=25.67, default_y=-115.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-110.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=61.95, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.96, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=134.23, default_y=-110.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=164.24, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=194.25, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=224.25, default_y=-110.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=254.26, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=284.27, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='4', width=309.68):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(134.58)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.74, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=162.85, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=235.47, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.74, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=162.85, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=235.47, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.74, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=104.94, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=129.15, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=162.85, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=187.05, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=211.26, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=235.47, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=259.67, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=283.88, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='5', width=256.56):
            with Note(default_x=14.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=96.26, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=160.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=182.07, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=206.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=230.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=96.26, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=182.07, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=96.26, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=182.07, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=38.3, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=62.59, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=96.26, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=120.56, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=144.85, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=182.07, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=206.36, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=230.66, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='6', width=245.33):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=128.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=168.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=193.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=218.73, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=10.0, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=87.39, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=168.73, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=87.03, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=10.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=35.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=60.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=87.39, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=112.39, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=143.73, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=168.73, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=193.73, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=218.73, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='7', width=244.92):
            with Note(default_x=25.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=172.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=196.19, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=219.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=26.03, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=96.73, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=172.62, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=26.03, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=96.73, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=172.62, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-39.49)
            with Backup():
                Duration(1440.0)
            with Note(default_x=26.03, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=49.6, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=73.17, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=96.73, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=120.3, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=143.87, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=172.62, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=196.19, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.75, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='8', width=411.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(134.58)
                with StaffLayout(number=2):
                    StaffDistance(74.62)
            with Note(default_x=116.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=306.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=337.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=387.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=208.11, default_y=-94.62):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=306.86, default_y=-94.62):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=116.5, default_y=-164.62):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-36.12, default_y=0.51)
            with Note(default_x=116.5, default_y=-144.62):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-36.12, default_y=0.51)
            with Note(default_x=116.5, default_y=-119.62):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-36.12, default_y=0.51)
            with Note(default_x=208.11, default_y=-119.62):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=306.86, default_y=-119.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=116.5, default_y=-119.62):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=147.04, default_y=-109.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=177.58, default_y=-109.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=208.11, default_y=-119.62):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=238.65, default_y=-109.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=269.19, default_y=-109.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=306.86, default_y=-109.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=337.4, default_y=-104.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=367.94, default_y=-104.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='9', width=341.37):
            with Note(default_x=11.75, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=30.19, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=225.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Tuplet(type='start', number=1, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('eighth')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('eighth')
                    with Tuplet(type='start', number=2, bracket='no'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('16th')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('16th')
            with Note(default_x=241.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop', number=2)
            with Note(default_x=274.9, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop', number=1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=30.55, default_y=-89.62):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=127.86, default_y=-89.62):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=225.16, default_y=-94.62):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=30.19, default_y=-124.62):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=30.55, default_y=-114.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=62.99, default_y=-104.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.42, default_y=-104.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=127.86, default_y=-114.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=160.29, default_y=-104.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=192.73, default_y=-104.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=225.16, default_y=-114.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=274.9, default_y=-104.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=307.33, default_y=-104.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='10', width=303.34):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Tuplet(type='start', number=1, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('eighth')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('eighth')
                    with Tuplet(type='start', number=2, bracket='no'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('16th')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('16th')
            with Note(default_x=29.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=45.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop', number=2)
            with Note(default_x=60.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop', number=1)
            with Note(default_x=118.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=204.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-99.62):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=118.38, default_y=-94.62):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=204.76, default_y=-104.62):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.44, default_y=-124.62):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=216.62, default_y=-124.62):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-114.62):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=60.8, default_y=-109.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.59, default_y=-109.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=118.38, default_y=-119.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=147.17, default_y=-109.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=175.97, default_y=-109.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=204.76, default_y=-119.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=244.15, default_y=-109.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=272.95, default_y=-109.62):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='11', width=415.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(134.58)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=170.89, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=201.61, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=305.53, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=201.61, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=305.53, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=92.24, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=317.4, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=120.5, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=155.14, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=201.61, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=236.25, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=270.89, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=305.53, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=344.93, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=379.57, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='12', width=292.95):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.16, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=109.0, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=200.18, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.16, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=108.64, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.16, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=44.55, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=74.94, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=109.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=139.39, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.79, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=200.18, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=230.57, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=260.96, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='13', width=347.73):
            with Note(default_x=20.0, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=239.9, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=20.36, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=126.59, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=239.9, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=20.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=239.9, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=20.36, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=55.77, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.18, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=126.59, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=162.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=197.4, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=239.9, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=275.31, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=310.72, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='14', width=414.24):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(134.58)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=143.83, default_y=10.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=154.79, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.76, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=176.73, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=188.44, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=304.58, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=188.44, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=304.58, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=188.44, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=304.58, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=116.4, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=152.42, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=188.44, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=224.46, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=260.48, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=304.58, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=340.6, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=376.62, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='15', width=321.24):
            with Note(default_x=11.75, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=30.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=126.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=223.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=126.68, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=223.16, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=30.19, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=126.68, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=223.16, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=30.19, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=62.35, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.51, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=126.68, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=158.84, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.0, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=223.16, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=255.32, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=287.48, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='16', width=321.01):
            with Note(default_x=19.64, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=20.0, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=133.19, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=226.3, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=31.87, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=226.3, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=20.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=71.12, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=102.15, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=133.19, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=164.23, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.26, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=226.3, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=257.34, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=288.37, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='17', width=347.29):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=95.38, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=262.38, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=95.38, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=262.38, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=95.38, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=262.38, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=96.11, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=123.52, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.29, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=179.06, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=206.83, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=234.6, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=262.38, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=290.15, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=317.92, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='18', width=321.85):
            with Note(default_x=25.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=74.94, default_y=10.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=85.9, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=107.49, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=118.46, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=130.17, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=227.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=25.83, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=130.17, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=227.48, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=25.83, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=130.17, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=227.48, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=25.83, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=56.76, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=87.68, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=130.17, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=161.1, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=192.02, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=227.48, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=258.41, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=289.33, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='19', width=387.35):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=143.24, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=257.97, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(360.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=351.84, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=143.24, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=257.97, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=26.17, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=66.75, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=104.99, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=143.24, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=181.48, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.72, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=257.97, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=296.21, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=334.45, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Forward():
                Duration(480.0)
            with Note(default_x=143.24, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(480.0)
                Voice('8')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(480.0)
        with Measure(number='20', width=445.28):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(96.16)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=167.2, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Forward():
                Duration(960.0)
            with Note(default_x=256.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=276.96, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=297.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=329.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=349.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=369.97, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=402.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=422.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=254.74, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=167.56, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=254.74, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=109.44, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=138.5, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=167.56, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=196.62, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=225.68, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=254.74, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=311.84, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=383.66, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='21', width=337.88):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=133.96, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=229.08, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(360.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=308.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=133.96, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=229.08, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=29.97, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=70.55, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=102.26, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=133.96, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=165.67, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=197.38, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=229.08, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=260.79, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=292.49, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Forward():
                Duration(480.0)
            with Note(default_x=133.96, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(480.0)
                Voice('8')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('8')
                Type('quarter')
                Staff(2)
        with Measure(number='22', width=273.33):
            with Note(default_x=13.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=185.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=99.78, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=185.76, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.44, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=42.46, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=71.12, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=99.78, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=128.44, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=157.1, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=185.76, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=214.41, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=243.07, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='23', width=556.83):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(96.16)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=238.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=397.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.74, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=238.9, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=397.06, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.74, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=133.46, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=186.18, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=238.9, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=291.62, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=344.34, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=397.06, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=449.78, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=502.51, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='24', width=499.67):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=169.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=169.04, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=25.67, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=180.9, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=91.42, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=169.04, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=246.65, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('7')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(480.0)
                Voice('7')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='25', width=1056.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(96.16)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Key():
                    Fifths(-4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Con fuoco. ', relative_y=20.0, font_weight='bold', font_size='12')
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('84')
                Staff(1)
                Sound(tempo=84.0)
            with Note(default_x=114.18, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=114.18, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=166.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.44, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=218.7, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.7, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=270.96, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.96, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=323.23, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=323.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=375.49, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=375.49, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=427.75, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=427.75, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=480.01, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=480.01, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=532.27, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=532.27, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=584.54, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=584.54, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=636.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=636.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=689.06, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=689.06, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=741.32, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=741.32, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=793.58, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=793.58, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=845.85, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=845.85, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=898.11, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=898.11, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=950.37, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=950.37, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=1002.63, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=1002.63, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=114.18, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=166.44, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.7, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.96, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=323.23, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=375.49, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=427.75, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=480.01, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=532.27, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=584.54, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=636.8, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=689.06, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=741.32, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=793.58, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=845.85, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=898.11, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=950.37, default_y=-170.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=1002.63, default_y=-175.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=114.18, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(960.0)
        with Measure(number='26', width=595.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(96.16)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=114.18, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=114.18, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=140.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.46, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=166.74, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.74, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=193.02, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.02, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=219.3, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.3, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=245.58, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=245.58, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=278.42, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=278.42, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=304.7, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.7, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=330.98, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.98, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=357.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=357.26, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=383.54, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=383.54, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=409.82, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=409.82, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=436.1, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=436.1, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=462.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=462.38, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=488.66, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=488.66, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=514.94, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=514.94, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=541.22, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=541.22, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=567.5, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=567.5, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=114.18, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=140.46, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.74, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.02, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.3, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note():
                Rest()
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(2)
            with Note(default_x=262.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=278.42, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='27', width=461.12):
            with Note(default_x=13.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=13.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=38.19, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=38.19, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=62.57, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.57, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=86.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.96, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=111.35, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.35, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=135.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=135.73, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=160.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=160.12, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=184.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.51, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=208.89, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.89, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=235.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.56, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=259.94, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.94, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=288.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=288.81, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=313.2, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=313.2, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=337.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=337.58, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=361.97, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=361.97, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=386.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=386.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=410.74, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=410.74, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=435.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=435.13, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=38.19, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.57, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.96, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.35, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.73, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=160.12, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=184.51, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.89, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.56, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.94, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=288.81, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=313.2, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=337.58, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=361.97, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=386.36, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=410.74, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=435.13, default_y=-170.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(960.0)
        with Measure(number='28', width=603.87):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(96.16)
                with StaffLayout(number=2):
                    StaffDistance(87.5)
            with Note(default_x=121.58, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=121.58, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=150.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.45, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=175.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.59, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=200.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.73, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=229.6, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=229.6, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=254.74, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=254.74, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=293.72, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=293.72, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=318.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=318.86, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=344.0, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=344.0, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=369.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=369.14, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=394.29, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=394.29, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=419.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=419.43, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=449.89, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=449.89, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=476.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=476.56, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=501.7, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=501.7, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=526.84, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=526.84, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=551.98, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=551.98, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=577.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=577.13, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.58, default_y=-207.5):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=150.45, default_y=-167.5):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.59, default_y=-152.5):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.73, default_y=-142.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=229.6, default_y=-132.5):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note():
                Rest()
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(2)
            with Note(default_x=270.45, default_y=-117.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=293.72, default_y=-117.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='29', width=452.63):
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=13.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=40.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
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
            with Note(default_x=40.47, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=63.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.82, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=87.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.18, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=110.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.54, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=141.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=141.87, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=165.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=165.23, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=188.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.58, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=211.94, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.94, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=235.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.3, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=258.66, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.66, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=282.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=282.02, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=305.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=305.37, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=334.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.24, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=357.6, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=357.6, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=380.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=380.95, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=404.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=404.31, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=427.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=427.67, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-117.5):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=126.2, default_y=-112.5):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=165.23, default_y=-122.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=305.37, default_y=-127.5):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.44, default_y=-147.5):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1440.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='30', width=585.72):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(77.5)
            with Note(default_x=110.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=110.74, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=139.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.6, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=164.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.97, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=190.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.33, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=215.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.69, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=247.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=247.4, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=276.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=276.26, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=305.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.13, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=330.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.49, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=355.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=355.85, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=381.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.22, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=406.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=406.58, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=431.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=431.94, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=457.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=457.3, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=482.67, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=482.67, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=508.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=508.03, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=533.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=533.39, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=558.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=558.75, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=110.74, default_y=-117.5):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=231.54, default_y=-112.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=276.26, default_y=-122.5):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=431.94, default_y=-127.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(1440.0)
            with Note(default_x=110.38, default_y=-137.5):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1440.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='31', width=470.78):
            with Note(default_x=16.92, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=130.6, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=175.13, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=322.15, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=16.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=41.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=175.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=199.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=322.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=346.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=371.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=395.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=420.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=444.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=16.92, default_y=-127.5):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=175.13, default_y=-122.5):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=322.15, default_y=-117.5):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=16.56, default_y=-157.5):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=16.56, default_y=-137.5):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1440.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='32', width=555.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(93.2)
                with StaffLayout(number=2):
                    StaffDistance(73.15)
            with Note(default_x=121.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=265.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=145.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=265.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=289.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=337.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=361.94, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=385.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=410.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=434.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=458.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=482.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=506.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=530.19, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.58, default_y=-108.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=265.8, default_y=-113.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=410.01, default_y=-98.15):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.22, default_y=-133.15):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1440.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='33', width=500.67):
            with Note(default_x=25.24, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=144.54, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=189.53, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=344.3, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=25.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=51.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=189.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=215.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=318.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=344.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=370.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=395.89, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=421.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=447.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=473.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=6.8, default_y=-168.15):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=25.24, default_y=-123.15):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=189.53, default_y=-118.15):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=344.3, default_y=-113.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Forward():
                Duration(480.0)
            with Note(default_x=189.17, default_y=-133.15):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='34', width=522.8):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(93.2)
                with StaffLayout(number=2):
                    StaffDistance(73.15)
            with Note(default_x=121.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=252.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=143.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=252.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=274.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.48, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=318.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=340.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=362.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=383.92, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=405.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=427.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=449.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=471.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=498.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.58, default_y=-108.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=252.75, default_y=-113.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=383.92, default_y=-98.15):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.22, default_y=-133.15):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1440.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='35', width=533.69):
            with Note(default_x=37.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=63.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=199.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=225.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=250.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.64, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=331.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=357.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=357.27, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=383.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=408.9, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=434.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=460.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=460.53, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=486.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=37.99, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(360.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=157.38, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=199.33, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=4.75, default_y=-138.15):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(3)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=37.99, default_y=-93.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=63.81, default_y=-103.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.62, default_y=-93.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.44, default_y=-103.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.25, default_y=-93.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.52, default_y=-103.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=199.33, default_y=-123.15):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=199.33, default_y=-88.15):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='36', width=470.5):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(93.2)
                with StaffLayout(number=2):
                    StaffDistance(65.4)
            with Attributes():
                with Time():
                    Beats('6')
                    BeatType('8')
            with Note(default_x=134.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=189.85, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=245.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=301.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=357.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=413.17, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=134.12, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=161.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.85, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.58, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=301.31, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=329.17, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=357.04, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=384.9, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=413.17, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=441.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(1440.0)
            with Note():
                Rest(measure='yes')
                Duration(1440.0)
                Voice('5')
                Staff(2)
        with Measure(number='37', width=585.99):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Note(default_x=34.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=34.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=65.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.2, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=95.61, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.61, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=126.01, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.01, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=156.42, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.42, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=186.82, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=186.82, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=217.22, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=217.22, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=247.63, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.63, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=278.03, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.03, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=308.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=308.44, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=338.84, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=338.84, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=369.3, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=369.3, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=399.71, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=399.71, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=432.37, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=432.37, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=462.78, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=462.78, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=493.18, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=493.18, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=523.59, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=523.59, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=553.99, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=553.99, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=34.8, default_y=-130.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=65.2, default_y=-135.4):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.61, default_y=-130.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.01, default_y=-125.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.42, default_y=-130.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.82, default_y=-135.4):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=217.22, default_y=-130.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=247.63, default_y=-135.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.03, default_y=-140.4):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=308.44, default_y=-145.4):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=338.84, default_y=-150.4):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=369.3, default_y=-155.4):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=399.71, default_y=-150.4):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=432.37, default_y=-155.4):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=462.78, default_y=-160.4):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=493.18, default_y=-165.4):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=523.59, default_y=-170.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=553.99, default_y=-175.4):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=34.8, default_y=-150.4):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(960.0)
        with Measure(number='38', width=595.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(93.2)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=114.18, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=114.18, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=140.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.46, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=166.74, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.74, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=193.02, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.02, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=219.3, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.3, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=245.58, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=245.58, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=278.42, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=278.42, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=304.7, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.7, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=330.98, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.98, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=357.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=357.26, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=383.54, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=383.54, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=409.82, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=409.82, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=436.1, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=436.1, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=462.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=462.38, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=488.66, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=488.66, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=514.94, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=514.94, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=541.22, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=541.22, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=567.5, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=567.5, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=114.18, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=140.46, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.74, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.02, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.3, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note():
                Rest()
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(2)
            with Note(default_x=262.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=278.42, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='39', width=461.12):
            with Note(default_x=13.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=13.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=38.19, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=38.19, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=62.57, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.57, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=86.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.96, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=111.35, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.35, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=135.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=135.73, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=160.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=160.12, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=184.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.51, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=208.89, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.89, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=235.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.56, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=259.94, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.94, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=288.81, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=288.81, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=313.2, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=313.2, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=337.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=337.58, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=361.97, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=361.97, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=386.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=386.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=410.74, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=410.74, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=435.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=435.13, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=38.19, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.57, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.96, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.35, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.73, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=160.12, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=184.51, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.89, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.56, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.94, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=288.81, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=313.2, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=337.58, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=361.97, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=386.36, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=410.74, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=435.13, default_y=-170.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(960.0)
        with Measure(number='40', width=608.99):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(93.2)
                with StaffLayout(number=2):
                    StaffDistance(73.08)
            with Note(default_x=121.58, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=121.58, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=150.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.45, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=175.97, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.97, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=201.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.49, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=230.35, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.35, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=255.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=255.87, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=295.08, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=295.08, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=320.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=320.6, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=346.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=346.12, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=371.64, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=371.64, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=397.15, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=397.15, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=422.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=422.67, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=453.14, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=453.14, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=479.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=479.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=505.32, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=505.32, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=530.84, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=530.84, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=556.36, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=556.36, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=581.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=581.87, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.58, default_y=-193.08):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=150.45, default_y=-153.08):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.97, default_y=-138.08):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.49, default_y=-128.08):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.35, default_y=-118.08):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note():
                Rest()
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Staff(2)
            with Note(default_x=271.82, default_y=-103.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=295.08, default_y=-103.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='41', width=447.5):
            with Note(default_x=16.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=16.2, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=45.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=45.07, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=68.15, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.15, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=91.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.24, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=114.33, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.33, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=145.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=145.66, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=168.75, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=168.75, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=191.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.84, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=214.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.93, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=238.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.02, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=261.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=261.11, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=284.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=284.2, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=307.29, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=307.29, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=330.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.38, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=353.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=353.47, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=376.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=376.56, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=399.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=399.65, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=422.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=422.74, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=20.86, default_y=-128.08):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=130.0, default_y=-123.08):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=168.75, default_y=-133.08):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=307.29, default_y=-138.08):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.84, default_y=-148.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=15.84, default_y=-113.08):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='42', width=581.09):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=122.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=122.98, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=151.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.84, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=176.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.61, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=201.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.38, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=226.15, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.15, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=257.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=257.48, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=282.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=282.25, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=307.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=307.02, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=331.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=331.79, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=356.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=356.56, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=381.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.33, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=406.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=406.1, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=430.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=430.87, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=455.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=455.64, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=480.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=480.41, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=505.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=505.18, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=529.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=529.95, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=554.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=554.72, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=122.98, default_y=-170.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=122.98, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=241.82, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=241.82, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=281.89, default_y=-175.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=281.89, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(960.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='43', width=475.41):
            with Note():
                Rest()
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=36.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.34, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=63.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=88.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.28, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=113.56, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=113.56, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=145.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=145.16, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=170.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=170.44, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=195.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.72, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=221.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=246.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=246.28, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=271.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.56, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=296.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=296.84, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=322.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=322.13, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=347.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=347.41, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=372.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=372.69, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=397.97, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=397.97, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=423.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=423.25, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=448.53, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=448.53, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=15.72, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=129.36, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=170.44, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=322.13, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=10.7, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.7, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='44', width=503.29):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.59)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=126.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=126.22, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=146.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.28, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=166.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.34, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=186.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.4, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=206.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.46, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=237.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=237.79, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=257.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=257.85, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=277.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.92, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=297.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.98, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=318.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=318.04, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=338.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=338.1, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=358.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=358.16, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=378.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=378.22, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=398.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=398.28, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=418.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=418.34, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=438.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=438.4, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=458.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=458.46, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Note(default_x=478.53, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=478.53, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=126.22, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=126.22, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=222.13, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=222.13, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=257.49, default_y=-170.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(960.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=257.49, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(960.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
        with Measure(number='45', width=553.2):
            with Note(default_x=37.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=172.69, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=218.09, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=386.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=508.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
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
            with Note(default_x=37.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=64.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=218.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=244.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=323.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=350.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=386.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=412.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=439.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=465.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=492.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=525.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=4.75, default_y=-135.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=37.99, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=64.45, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.91, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.37, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.82, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.23, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=218.09, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=218.09, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
            with Note(default_x=244.55, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.01, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.47, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=323.92, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=350.38, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=367.8, default_y=-135.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=386.24, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=412.7, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=439.16, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=465.61, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=492.07, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=525.15, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='46', width=576.77):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.59)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=121.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=278.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=390.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=430.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
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
            with Note(default_x=121.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=145.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=278.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=302.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=326.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=350.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=374.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=406.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=430.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=454.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=478.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=502.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=526.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=551.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=121.58, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=121.58, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
            with Note(default_x=145.73, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.88, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.03, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.18, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.33, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=259.75, default_y=-140.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=278.19, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=302.34, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=326.49, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=350.64, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=374.79, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=406.12, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=430.27, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=430.27, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
            with Note(default_x=454.42, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=478.57, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=502.72, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=526.87, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=551.02, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='47', width=479.72):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=174.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=282.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=320.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=36.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.42, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=174.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=198.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=244.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=298.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=320.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=343.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=366.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=389.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=412.21, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=435.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=36.61, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.42, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.23, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.04, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.85, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=145.26, default_y=-150.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Octave(2)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=174.71, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=198.4, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.21, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=244.02, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.83, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=298.16, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=320.97, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=320.97, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
            with Note(default_x=343.78, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=366.59, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=389.4, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=412.21, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=435.02, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='48', width=437.65):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.59)
                with StaffLayout(number=2):
                    StaffDistance(65.35)
            with Attributes():
                with Time():
                    Beats('6')
                    BeatType('8')
            with Note(default_x=130.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(720.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=281.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=380.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=130.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.96, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=229.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=281.08, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=305.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=355.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=380.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=405.63, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=130.32, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.14, default_y=-115.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.96, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.77, default_y=-115.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=229.59, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.41, default_y=-115.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=281.08, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=305.9, default_y=-115.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=330.71, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=355.53, default_y=-115.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=380.35, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=405.63, default_y=-115.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='49', width=363.59):
            with Attributes():
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Tempo I ', default_x=-63.81, relative_y=20.0, font_weight='bold', font_size='12')
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-63.81, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=53.66, default_y=-50.0):
                Grace()
                with Pitch():
                    Step('C')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=64.62, default_y=-35.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=75.59, default_y=-25.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=87.3, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=270.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=179.11, default_y=-80.35):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=270.55, default_y=-85.35):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=87.67, default_y=-150.35):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=118.15, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=148.63, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=179.11, default_y=-105.35):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=209.59, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=240.07, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=270.55, default_y=-105.35):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=301.03, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=331.51, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='50', width=255.26):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=93.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=173.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-90.35):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=93.75, default_y=-85.35):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=173.71, default_y=-95.35):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.44, default_y=-115.35):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-105.35):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=40.45, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.1, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=93.75, default_y=-110.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=120.4, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=147.06, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=173.71, default_y=-110.35):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=200.36, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=227.01, default_y=-100.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='51', width=420.74):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.59)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=179.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=210.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=314.62, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=210.1, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=314.62, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=92.24, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=128.53, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.37, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=210.1, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=244.94, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=279.78, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=314.62, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=349.46, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=384.3, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='52', width=311.15):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.16, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=113.28, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=211.42, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.16, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=113.28, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=211.42, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.16, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=46.87, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=79.58, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=113.28, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=145.99, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=178.7, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=211.42, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=244.13, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=276.84, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='53', width=324.6):
            with Note(default_x=14.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=113.52, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=195.03, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=224.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=257.15, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=290.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=113.52, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=224.23, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=113.52, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=224.23, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=14.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=46.92, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=79.85, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=113.52, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=146.44, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=179.36, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=224.23, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=257.15, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=290.08, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='54', width=411.62):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.59)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=204.31, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=249.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(69.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=268.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(69.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(69.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=318.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(69.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(69.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=368.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(69.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=386.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(69.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=158.9, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=249.71, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=158.54, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=105.94, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=131.51, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=158.9, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=184.47, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=224.15, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=249.71, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=302.62, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=352.57, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='55', width=250.75):
            with Note(default_x=26.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=134.86, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=179.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(160.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=202.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=225.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=26.03, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=95.9, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=179.28, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=26.03, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=95.9, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=179.28, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-39.49)
            with Backup():
                Duration(1440.0)
            with Note(default_x=26.03, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=49.32, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=72.61, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=95.9, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=119.19, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.52, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=179.28, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=202.57, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=225.86, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='56', width=394.13):
            with Note(default_x=38.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=229.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(160.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='start', number=1, bracket='no', show_number='none')
            with Note(default_x=259.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(53.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    with Tuplet(type='start', number=2, bracket='no'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('16th')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('16th')
            with Note(default_x=286.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(53.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=302.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop', number=2)
            with Note(default_x=319.59, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=338.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Tuplet(type='start', number=2, bracket='no'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('16th')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('16th')
            with Note(default_x=353.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=369.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop', number=1)
                    Tuplet(type='stop', number=2)
            with Backup():
                Duration(1440.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=130.65, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=229.33, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=39.12, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-36.12, default_y=0.51)
            with Note(default_x=39.12, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-36.12, default_y=0.51)
            with Note(default_x=39.12, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-36.12, default_y=0.51)
            with Note(default_x=130.65, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=229.33, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=39.12, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=69.63, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=100.14, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=130.65, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=161.16, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.67, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=229.33, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=259.85, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=338.03, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='57', width=409.06):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=286.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Tuplet(type='start', number=1, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('eighth')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('eighth')
                    with Tuplet(type='start', number=2, bracket='no'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('16th')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('16th')
            with Note(default_x=303.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=321.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop', number=2)
            with Note(default_x=338.92, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop', number=1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.74, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=183.55, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=286.37, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.74, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=115.01, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=149.28, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=183.55, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=217.82, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=252.1, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=286.37, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=338.92, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=373.19, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='58', width=320.85):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Tuplet(type='start', number=1, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('eighth')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('eighth')
                    with Tuplet(type='start', number=2, bracket='no'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('16th')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('16th')
            with Note(default_x=29.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=45.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(53.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop', number=2)
            with Note(default_x=61.61, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='stop', number=1)
            with Note(default_x=123.96, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=217.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=123.96, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=217.5, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.44, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=229.36, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=61.61, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.79, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=123.96, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=155.14, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=186.32, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=217.5, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=256.89, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=288.07, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='59', width=326.58):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=100.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=128.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=222.86, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=128.76, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=222.86, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=25.67, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=234.72, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=53.92, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=85.28, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=128.76, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=160.13, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.49, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=222.86, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=262.25, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=293.62, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='60', width=352.25):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.66)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.74, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=173.76, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=262.21, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.74, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=173.4, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.74, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=110.22, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=139.7, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=173.76, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=203.24, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=232.73, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=262.21, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=291.69, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=321.17, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='61', width=340.45):
            with Note(default_x=20.0, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=235.35, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=20.36, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=123.86, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=235.35, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=20.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=235.35, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=20.36, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=54.86, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.36, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=123.86, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=158.36, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=192.86, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=235.35, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=269.85, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=304.35, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='62', width=363.79):
            with Note(default_x=13.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=83.3, default_y=10.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=94.26, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=105.23, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=116.19, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=127.91, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=248.08, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=127.91, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=248.08, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=127.91, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=248.08, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=51.84, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.87, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=127.91, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=165.95, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.98, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=248.08, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=286.12, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=324.15, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='63', width=334.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.66)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=98.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=176.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=254.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=176.74, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=254.66, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=98.82, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=176.74, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=254.66, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=98.82, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=124.79, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.77, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=176.74, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=202.72, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=228.69, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=254.66, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=280.64, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=306.61, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='64', width=265.32):
            with Note(default_x=19.64, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=20.0, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=117.37, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=186.76, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=31.87, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=186.76, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=20.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=71.12, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.25, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=117.37, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=140.5, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.63, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=186.76, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=217.43, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=240.56, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='65', width=203.34):
            with Note(default_x=19.64, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=138.93, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=19.64, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=138.93, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=19.64, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=138.93, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=20.36, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=39.83, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=59.65, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=79.47, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=99.29, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=119.11, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=138.93, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=158.75, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=178.57, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='66', width=253.64):
            with Note(default_x=25.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=54.79, default_y=10.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=65.75, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=87.34, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=98.31, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=110.02, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=187.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=25.83, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=110.02, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=187.18, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=25.83, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=110.02, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=187.18, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=25.83, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=46.68, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.53, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=110.02, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=130.87, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.72, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=187.18, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=208.03, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=228.88, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='67', width=529.51):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.66)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=230.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=371.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(360.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=486.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=230.83, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=371.37, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=96.54, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=137.13, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.98, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=230.83, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=277.67, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=324.52, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=371.37, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=418.22, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=465.07, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Forward():
                Duration(480.0)
            with Note(default_x=230.83, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(480.0)
                Voice('8')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(480.0)
        with Measure(number='68', width=526.98):
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=138.89, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Forward():
                Duration(960.0)
            with Note(default_x=266.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=295.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=324.96, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=364.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=393.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=409.1, default_y=-5.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=429.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=469.08, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=498.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=264.71, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.26, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=264.71, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=55.62, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=97.44, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=139.26, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=181.07, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=222.89, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=264.71, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=346.88, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=443.21, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='69', width=456.68):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.66)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=84.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=216.25, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=329.24, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(360.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=421.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1440.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=216.25, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=329.24, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=100.34, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=84.18, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=140.93, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=178.59, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=216.25, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=253.91, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=291.58, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=329.24, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=366.9, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=404.56, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1440.0)
            with Forward():
                Duration(480.0)
            with Note(default_x=216.25, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(480.0)
                Voice('8')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('8')
                Type('quarter')
                Staff(2)
        with Measure(number='70', width=321.76):
            with Note(default_x=13.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=218.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=115.92, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=218.04, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.44, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=47.84, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.88, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=115.92, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=149.96, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=184.0, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=218.04, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=252.08, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=286.12, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='71', width=278.06):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=101.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=188.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=101.35, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=188.9, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.44, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=13.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=42.98, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=72.17, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=101.35, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=130.54, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=159.72, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=188.9, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=218.09, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=247.27, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='72', width=395.6):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.66)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=194.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=294.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=194.9, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=294.45, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=92.24, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Backup():
                Duration(1440.0)
            with Note(default_x=80.38, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=128.53, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=161.71, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=194.9, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=228.08, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=261.26, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=294.45, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=327.63, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=360.82, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(160.0)
                Voice('7')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='73', width=344.75):
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Staff(1)
            with Note(default_x=113.54, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=133.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=154.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=172.15, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=11.97, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=32.29, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=52.6, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=72.92, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=93.23, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='74', width=316.15):
            with Note(print_object='no'):
                Rest()
                Duration(69.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(69.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(69.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Staff(1)
            with Note(default_x=80.4, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(69.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(69.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=126.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(69.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(69.0)
                Voice('1')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=169.3, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=11.97, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(69.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=34.78, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(69.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=57.59, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(69.0)
                Voice('5')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(69.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(69.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(69.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(69.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(2)
                Staff(2)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')