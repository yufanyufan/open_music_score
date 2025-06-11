with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Nocturne Op.72. No.1.')
    with Identification():
        Creator('F.Chopin', type='composer')
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
            Millimeters(5.456)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2176.9)
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
        CreditWords('Nocturne', default_x=770.014, default_y=2103.59, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('F.Chopin,Op.72.No.1', default_x=1466.71, default_y=1969.06, justify='right', valign='bottom', font_size='12')
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
                Volume(37.0079)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=664.57):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(120.1)
                        RightMargin(0.0)
                    TopSystemDistance(194.89)
                with StaffLayout(number=2):
                    StaffDistance(93.79)
            with Attributes():
                Divisions(480.0)
                with Key():
                    Fifths(1)
                with Time(symbol='common'):
                    Beats('4')
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
                    with Dynamics(default_x=7.5, default_y=-40.0, relative_x=1.94, relative_y=-30.27):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Andante', relative_x=-48.18, relative_y=43.8, font_weight='bold', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=-1.9, relative_y=-38.8):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note():
                Rest(measure='yes')
                Duration(1920.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(320.0)
                Voice('2')
                Type('quarter', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(print_object='no'):
                Rest()
                Duration(80.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Staff(1)
            with Note(default_x=636.52, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1920.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('molto legato', relative_x=27.25, relative_y=72.87, font_style='italic', font_size='11')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=105.72, default_y=-183.79):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=151.21, default_y=-163.79):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.7, default_y=-138.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=242.19, default_y=-148.79):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=287.68, default_y=-123.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=333.17, default_y=-128.79):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=378.66, default_y=-183.79):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=424.15, default_y=-163.79):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=469.64, default_y=-138.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=515.13, default_y=-148.79):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=560.62, default_y=-123.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=58.15)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=606.11, default_y=-128.79):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=-1.73, relative_y=-20.62):
                        BeatUnit('quarter')
                        PerMinute('66')
                Offset(-1760.0)
                Staff(1)
                Sound(tempo=66.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('( ', relative_x=-51.7, relative_y=22.68, font_weight='bold', font_size='12')
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=-51.7, relative_y=22.68):
                        BeatUnit('quarter')
                        PerMinute('69')
                with DirectionType():
                    Words(' )', relative_x=-51.7, relative_y=22.68, font_weight='bold', font_size='12')
                Offset(-1600.0)
                Staff(1)
                Sound(tempo=69.0)
        with Measure(number='2', width=608.72):
            with Note(default_x=13.75, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=32.19, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=454.69, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=530.91, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=32.55, default_y=-183.79):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=79.46, default_y=-163.79):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=126.36, default_y=-138.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=173.26, default_y=-148.79):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=220.17, default_y=-123.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=267.07, default_y=-128.79):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-82.86)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=313.98, default_y=-183.79):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=360.88, default_y=-163.79):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=407.78, default_y=-138.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=454.69, default_y=-148.79):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=507.45, default_y=-123.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=560.22, default_y=-128.79):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='3', width=482.64):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(91.73)
            with Note(default_x=91.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=374.7, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=453.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=92.01, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=123.42, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=154.83, default_y=-131.73):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=186.24, default_y=-141.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=217.65, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=249.06, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=280.47, default_y=-171.73):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=311.88, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=343.29, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=374.7, default_y=-146.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=406.11, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=437.52, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='4', width=440.13):
            with Note(default_x=21.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=172.48, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=225.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=225.69, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=278.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=278.9, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=332.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=332.11, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=385.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=385.32, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.4)
                Staff(2)
            with Note(default_x=21.03, default_y=-186.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=53.78, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=86.52, default_y=-131.73):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=119.27, default_y=-141.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=152.01, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=192.94, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.4)
                Staff(2)
            with Note(default_x=225.69, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=262.53, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=299.37, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=332.11, default_y=-146.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=368.95, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=405.79, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='5', width=449.97):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-69.89)
                Staff(1)
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=17.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=61.11)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-72.8)
                Staff(1)
            with Note(default_x=122.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=122.82, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=228.4, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=228.4, default_y=-35.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-32.08)
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.4)
                Staff(2)
            with Note(default_x=17.23, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=52.43, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=87.62, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=122.82, default_y=-131.73):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=158.01, default_y=-136.73):
                with Pitch():
                    Step('G')
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
            with Note(default_x=193.21, default_y=-166.73):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.4)
                Staff(2)
            with Note(default_x=228.4, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=263.6, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=307.59, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=342.78, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=377.98, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=413.17, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='6', width=485.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(91.73)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-46.51, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=5.77, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=88.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=186.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=385.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=88.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=187.07, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.5)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.5)
                Staff(1)
            with Note(default_x=285.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=385.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.4)
                Staff(2)
            with Note(default_x=88.41, default_y=-171.73):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=121.3, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=154.18, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=187.07, default_y=-136.73):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=219.95, default_y=-111.73):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=252.84, default_y=-116.73):
                with Pitch():
                    Step('D')
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.4)
                Staff(2)
            with Note(default_x=285.72, default_y=-176.73):
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=318.61, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=352.3, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=385.19, default_y=-111.73):
                with Pitch():
                    Step('E')
                    Octave(4)
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=418.07, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=450.96, default_y=-141.73):
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='7', width=441.07):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.5, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=24.25, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Staff(1)
                Sound(tempo=67.0)
            with Note(default_x=226.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=24.05, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Staff(1)
                Sound(tempo=65.0)
            with Note(default_x=332.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=225.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-102.93)
                Staff(2)
            with Note(default_x=12.72, default_y=-161.73):
                with Pitch():
                    Step('B')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=48.28, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=83.85, default_y=-116.73):
                with Pitch():
                    Step('D')
                    Octave(4)
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
            with Note(default_x=119.41, default_y=-126.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=154.97, default_y=-101.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=190.54, default_y=-106.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-102.93)
                Staff(2)
            with Note(default_x=226.1, default_y=-111.73):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=261.66, default_y=-116.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=63.98)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=63.98)
                Staff(2)
            with Note(default_x=297.22, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=332.79, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=368.35, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=403.91, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='8', width=446.23):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=22.2, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=16.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=230.57, default_y=-15.0):
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
                Duration(1920.0)
            with Note(default_x=29.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=230.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-102.93)
                Staff(2)
            with Note(default_x=17.23, default_y=-176.73):
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=52.85, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=88.46, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=124.08, default_y=-111.73):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=159.7, default_y=-101.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.31, default_y=-106.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-31.93)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-102.93)
                Staff(2)
            with Note(default_x=230.93, default_y=-111.73):
                with Pitch():
                    Step('E')
                    Octave(4)
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=266.55, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=302.16, default_y=-131.73):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=337.78, default_y=-141.73):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=373.4, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=409.01, default_y=-211.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=10.72, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Offset(-480.0)
                Staff(1)
                Sound(tempo=66.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=1.73, relative_y=58.19):
                        BeatUnit('quarter')
                        PerMinute('63')
                Offset(-320.0)
                Staff(1)
                Sound(tempo=63.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.01, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Offset(-160.0)
                Staff(1)
                Sound(tempo=60.0)
        with Measure(number='9', width=521.11):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(161.26)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.62, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=83.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-80.8)
                Staff(1)
            with Note(default_x=192.44, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('rit.', relative_y=40.0, font_style='italic', font_size='11')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=42.59, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=301.46, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note(default_x=410.49, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=83.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(480.0)
                Voice('2')
                Type('quarter', size='cue')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(960.0)
                Voice('2')
                Type('half', size='cue')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=83.41, default_y=-266.26):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=119.75, default_y=-231.26):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=156.1, default_y=-211.26):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=192.44, default_y=-201.26):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=228.78, default_y=-191.26):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=265.12, default_y=-196.26):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=301.46, default_y=-206.26):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=337.8, default_y=-191.26):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=374.15, default_y=-196.26):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=410.49, default_y=-211.26):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=446.83, default_y=-191.26):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=483.17, default_y=-196.26):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='10', width=432.22):
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', relative_x=-0.72, relative_y=61.47, font_style='italic', font_size='11')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=26.93, relative_x=0.54, relative_y=55.06):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-45.8, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=77.78)
            with Note(default_x=15.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=15.44, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=320.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=320.57, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=375.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=375.59, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=15.8, default_y=-251.26):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=49.66, default_y=-231.26):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.53, default_y=-206.26):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=117.39, default_y=-216.26):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=151.25, default_y=-191.26):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.11, default_y=-196.26):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-25.54)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=218.98, default_y=-251.26):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=252.84, default_y=-231.26):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=286.7, default_y=-206.26):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=320.57, default_y=-216.26):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=354.43, default_y=-191.26):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=396.76, default_y=-196.26):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-29.8)
                Staff(2)
        with Measure(number='11', width=419.41):
            with Note(default_x=16.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=16.87, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=25.2, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Staff(1)
                Sound(tempo=67.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-159.21)
                Staff(1)
            with Note(default_x=217.52, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
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
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=217.52, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
                with Notations():
                    Tied(type='stop')
            with Note(default_x=250.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=250.9, default_y=-5.0):
                Chord()
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
            with Note(default_x=284.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=284.28, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Staff(1)
                Sound(tempo=65.0)
            with Note(default_x=317.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
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
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=317.67, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=351.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=351.05, default_y=5.0):
                Chord()
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
            with Note(default_x=384.43, default_y=-25.0):
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
            with Note(default_x=384.43, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=17.23, default_y=-246.26):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=50.61, default_y=-231.26):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.99, default_y=-201.26):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=117.38, default_y=-211.26):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=150.76, default_y=-191.26):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=184.14, default_y=-196.26):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-25.54)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=217.52, default_y=-241.26):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=250.9, default_y=-231.26):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=284.28, default_y=-206.26):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=317.67, default_y=-216.26):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=351.05, default_y=-191.26):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=384.43, default_y=-196.26):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-31.93)
                Staff(2)
        with Measure(number='12', width=736.37):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(160.0)
                with StaffLayout(number=2):
                    StaffDistance(91.73)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.37, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=95.45, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=336.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=35.21, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Staff(1)
                Sound(tempo=67.0)
            with Note(default_x=420.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=48.27, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Staff(1)
                Sound(tempo=65.0)
            with Note(default_x=578.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=630.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=682.71, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
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
            with Backup():
                Duration(1920.0)
            with Note(default_x=95.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(720.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=348.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=432.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=473.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=526.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=578.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=630.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=682.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('2')
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
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-102.93)
                Staff(2)
            with Note(default_x=95.45, default_y=-186.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=147.51, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=199.58, default_y=-131.73):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=251.64, default_y=-141.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=303.7, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=368.77, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-34.06)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-102.93)
                Staff(2)
            with Note(default_x=420.83, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=474.46, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=526.52, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=578.58, default_y=-146.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=630.65, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=682.71, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-42.57)
                Staff(2)
        with Measure(number='13', width=636.38):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=49.89, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=17.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=43.95, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Staff(1)
                Sound(tempo=64.0)
            with Note(default_x=171.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=171.62, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=223.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=223.08, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=274.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
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
            with Note(default_x=274.54, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=325.64, default_y=-35.0):
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
                    Slur(type='stop', number=1)
            with Note(default_x=325.64, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.4)
                Staff(2)
            with Note(default_x=17.23, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=68.69, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=120.16, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=171.62, default_y=-131.73):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=223.08, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.54, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.4)
                Staff(2)
            with Note(default_x=326.0, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=377.47, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=428.93, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=480.39, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=531.85, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=583.31, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='14', width=458.85):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    TopSystemDistance(75.8)
                with StaffLayout(number=2):
                    StaffDistance(107.01)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=88.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=367.01, default_y=-15.0):
                with Pitch():
                    Step('C')
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
                Duration(1920.0)
            with Note(default_x=88.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=179.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=227.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=276.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.2)
                Staff(2)
            with Note(default_x=88.77, default_y=-177.01):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=118.85, default_y=-212.01):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=148.93, default_y=-177.01):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=179.01, default_y=-167.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=212.85, default_y=-152.01):
                with Pitch():
                    Step('G')
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
            with Note(default_x=246.69, default_y=-142.01):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-37.0)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.2)
                Staff(2)
            with Note(default_x=276.77, default_y=-137.01):
                with Pitch():
                    Step('C')
                    Octave(4)
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=306.85, default_y=-142.01):
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
            with Note(default_x=336.93, default_y=-137.01):
                with Pitch():
                    Step('C')
                    Octave(4)
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
            with Note(default_x=367.01, default_y=-152.01):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=397.09, default_y=-162.01):
                with Pitch():
                    Step('E')
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
            with Note(default_x=427.17, default_y=-172.01):
                with Pitch():
                    Step('C')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='15', width=482.84):
            with Note(default_x=14.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=63.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=111.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=236.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-42.76, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=286.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=384.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=421.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=14.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=286.26, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('3')
                Type('quarter', size='cue')
                Staff(1)
            with Note(default_x=126.14, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=145.61, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=163.11, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=180.6, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=223.4, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(48.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('3')
                Type('eighth', size='cue')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('3')
                Type('half', size='cue')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.2)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=48.26)
                Staff(2)
            with Note(default_x=14.72, default_y=-187.01):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=30.39, default_y=-167.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.24, default_y=-152.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=111.91, default_y=-142.01):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=184.76, default_y=-127.01):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=263.35, default_y=-132.01):
                with Pitch():
                    Step('D')
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-5.46)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.2)
                Staff(2)
            with Note(default_x=286.62, default_y=-137.01):
                with Pitch():
                    Step('C')
                    Octave(4)
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=302.28, default_y=-172.01):
                with Pitch():
                    Step('C')
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
            with Note(default_x=352.06, default_y=-162.01):
                with Pitch():
                    Step('E')
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
            with Note(default_x=384.63, default_y=-152.01):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=419.51, default_y=-137.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=454.4, default_y=-127.01):
                with Pitch():
                    Step('E')
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='16', width=431.06):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-69.43, relative_x=3.73, relative_y=-13.33):
                        P()
                Staff(1)
                Sound(dynamics=44.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-80.24)
                Staff(1)
            with Note(default_x=21.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=119.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=172.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=225.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=323.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=376.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=32.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=32.9, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=224.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('poco                a                  poco', relative_y=64.77, font_style='italic', font_size='11')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.2)
                Staff(2)
            with Note(default_x=21.03, default_y=-137.01):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=53.71, default_y=-172.01):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=86.38, default_y=-162.01):
                with Pitch():
                    Step('E')
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
            with Note(default_x=119.05, default_y=-147.01):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=155.81, default_y=-122.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=192.57, default_y=-127.01):
                with Pitch():
                    Step('E')
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-33.04)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.2)
                Staff(2)
            with Note(default_x=225.25, default_y=-202.01):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=257.92, default_y=-167.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=290.59, default_y=-157.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=323.27, default_y=-147.01):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=360.03, default_y=-127.01):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=396.79, default_y=-132.01):
                with Pitch():
                    Step('D')
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-37.0)
                Staff(2)
        with Measure(number='17', width=520.46):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(215.0)
                with StaffLayout(number=2):
                    StaffDistance(91.73)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-46.77, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=61.11)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-86.77)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-86.77)
                Staff(1)
            with Note(default_x=95.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=199.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=255.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.02, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=77.78)
            with Note(default_x=311.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=415.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=427.04, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=107.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=107.32, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=311.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=95.45, default_y=-186.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=130.02, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=164.58, default_y=-141.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=199.15, default_y=-126.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=238.03, default_y=-101.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=276.92, default_y=-106.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-22.47)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=311.48, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=346.04, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=380.61, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=415.17, default_y=-126.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=449.74, default_y=-106.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=484.3, default_y=-111.73):
                with Pitch():
                    Step('E')
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-27.75)
                Staff(2)
        with Measure(number='18', width=444.35):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-46.77, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=12.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=24.12, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('67')
                Staff(1)
                Sound(tempo=67.0)
            with Note(default_x=227.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=239.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=0.18, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Staff(1)
                Sound(tempo=65.0)
            with Note(default_x=335.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.66)
                Staff(2)
            with Note(default_x=12.72, default_y=-176.73):
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=48.56, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=84.39, default_y=-116.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=120.23, default_y=-126.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=156.06, default_y=-101.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.9, default_y=-106.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-37.0)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.66)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=64.01)
                Staff(2)
            with Note(default_x=227.74, default_y=-176.73):
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=263.57, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=299.41, default_y=-116.73):
                with Pitch():
                    Step('D')
                    Octave(4)
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
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=335.24, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=371.08, default_y=-101.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=406.91, default_y=-106.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='19', width=407.93):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-46.59, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=77.78)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.43, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=26.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=216.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=311.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=26.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=216.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=26.75, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=58.38, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=90.02, default_y=-141.73):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=121.65, default_y=-126.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=153.28, default_y=-101.73):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=184.91, default_y=-106.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-22.47)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=216.54, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=248.17, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=279.8, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=311.44, default_y=-126.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=343.07, default_y=-106.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=374.7, default_y=-111.73):
                with Pitch():
                    Step('E')
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-26.43)
                Staff(2)
        with Measure(number='20', width=518.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(215.0)
                with StaffLayout(number=2):
                    StaffDistance(91.73)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=91.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=308.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(1920.0)
            with Note(default_x=104.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=196.03, default_y=-35.0):
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
            with Note(default_x=252.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=308.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=92.01, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=126.69, default_y=-156.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=161.36, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=196.03, default_y=-131.73):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=235.04, default_y=-116.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.04, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-35.68)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=308.72, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=343.39, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=378.06, default_y=-141.73):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=412.73, default_y=-126.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=447.4, default_y=-131.73):
                with Pitch():
                    Step('A')
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
            with Note(default_x=482.08, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-29.08)
                Staff(2)
        with Measure(number='21', width=440.04):
            with Note(default_x=21.39, default_y=-20.0):
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
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=19.95, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=229.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=21.39, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=15.02, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note(default_x=334.27, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=21.75, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=56.48, default_y=-156.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.2, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=125.92, default_y=-141.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=160.65, default_y=-131.73):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.37, default_y=-136.73):
                with Pitch():
                    Step('G')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-26.43)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=230.1, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=264.82, default_y=-156.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=299.54, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=334.27, default_y=-141.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=368.99, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=403.71, default_y=-141.73):
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-30.4)
                Staff(2)
        with Measure(number='22', width=414.36):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=16.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=16.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(960.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=17.23, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=50.19, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.15, default_y=-141.73):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=116.11, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=149.07, default_y=-156.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.03, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-27.75)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=214.99, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=247.95, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=280.92, default_y=-141.73):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=313.88, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=346.84, default_y=-156.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=379.8, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='23', width=535.55):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(215.0)
                with StaffLayout(number=2):
                    StaffDistance(91.73)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=91.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=91.65, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=304.63, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=304.63, default_y=-15.0):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=323.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=323.07, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=91.65, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=91.65, default_y=-10.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=193.91, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(320.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=193.91, default_y=-10.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(320.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=260.52, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(80.0)
                Tie(type='stop')
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=260.52, default_y=-10.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Tie(type='stop')
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=281.33, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=281.33, default_y=-15.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('3')
                Type('16th', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
            with Note(default_x=323.07, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=323.07, default_y=-15.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=425.33, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(320.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=425.33, default_y=-15.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(320.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=494.7, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Tie(type='stop')
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=494.7, default_y=-15.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Tie(type='stop')
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=515.52, default_y=-30.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('3')
                Type('16th', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=515.52, default_y=-20.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(80.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=92.01, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=125.32, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.63, default_y=-141.73):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=191.93, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=225.24, default_y=-156.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=258.54, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-22.47)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=323.43, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=356.74, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=390.05, default_y=-141.73):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=423.35, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=456.66, default_y=-156.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=489.96, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='24', width=405.9):
            with Note(default_x=24.37, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=24.37, default_y=-20.0):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=42.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=42.81, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=314.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=314.02, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=42.81, default_y=-30.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('none')
                Staff(1)
            with Note(default_x=42.81, default_y=-20.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1440.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('none')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('3')
                Type('quarter', size='cue')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=43.18, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=73.27, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=103.36, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=133.46, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=163.55, default_y=-156.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=193.64, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-27.75)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=223.74, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=253.83, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=283.92, default_y=-136.73):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=314.02, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=344.11, default_y=-156.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=374.2, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='25', width=431.3):
            with Note(default_x=29.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=29.26, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=174.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=174.52, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=34.82, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=225.56, default_y=-15.0):
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
            with Note(default_x=225.56, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=276.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=276.59, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=35.07, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note(default_x=327.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=327.63, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=378.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=378.67, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(print_object='no'):
                Rest()
                Duration(1440.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Staff(1)
            with Note(default_x=327.63, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=29.26, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=60.67, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.08, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=123.48, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=154.89, default_y=-156.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=194.15, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-31.72)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=225.56, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=256.96, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=296.22, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=327.63, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=359.04, default_y=-156.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=398.3, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='26', width=492.25):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(215.0)
                with StaffLayout(number=2):
                    StaffDistance(91.73)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=82.22)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=33.1, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=83.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=83.41, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=184.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=184.86, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=83.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('2')
                Type('half', size='cue')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=58.05)
                Staff(2)
            with Note(default_x=83.41, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=117.35, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.29, default_y=-141.73):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=185.22, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
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
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=219.16, default_y=-156.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=253.1, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-23.79)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=6.58, relative_y=40.0):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=287.03, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=320.97, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=354.91, default_y=-141.73):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=388.84, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=422.78, default_y=-156.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=456.72, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='27', width=444.87):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.82, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=16.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=16.87, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=225.9, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=225.9, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=225.9, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=386.75, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=386.75, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=398.62, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=17.23, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=52.01, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=86.79, default_y=-141.73):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=121.57, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=156.35, default_y=-156.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.12, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-29.08)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=225.9, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=260.68, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=295.46, default_y=-141.73):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=330.24, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=365.02, default_y=-156.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=408.49, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='28', width=435.62):
            with Note(default_x=35.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=135.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=334.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=32.58, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1920.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Note(default_x=32.58, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1920.0)
                Voice('2')
                Type('whole')
                Accidental('sharp')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=35.9, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=69.08, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=102.26, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=135.43, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=168.61, default_y=-156.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=201.79, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-26.43)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=234.96, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=268.14, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=301.32, default_y=-136.73):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=334.49, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=367.67, default_y=-156.73):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=400.85, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='29', width=730.61):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(186.63)
            with Note(default_x=91.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(1920.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=112.46, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(720.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=112.46, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(720.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-105.93)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-105.93)
                Staff(1)
            with Note(default_x=324.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=324.97, default_y=-35.0):
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
            with Note(default_x=405.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=405.78, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=486.59, default_y=-45.0):
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
            with Note(default_x=486.59, default_y=-35.0):
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
            with Note(default_x=567.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=567.4, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=648.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=648.21, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=94.97, default_y=-291.63):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=144.7, default_y=-256.63):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=194.43, default_y=-231.63):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=244.16, default_y=-241.63):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=293.89, default_y=-251.63):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=356.05, default_y=-256.63):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-51.54)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=405.78, default_y=-291.63):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=455.51, default_y=-256.63):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=517.67, default_y=-231.63):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=567.4, default_y=-241.63):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=617.12, default_y=-251.63):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=679.29, default_y=-256.63):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='30', width=642.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-65.93, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=13.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=13.64, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=35.26, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=152.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(320.0)
                Voice('2')
                Type('quarter', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('50')
                Staff(1)
                Sound(tempo=50.0)
            with Note(print_object='no'):
                Rest()
                Duration(80.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('40')
                Staff(1)
                Sound(tempo=40.0)
            with Note(default_x=598.36, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=619.34, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1920.0)
            with Note(print_object='no'):
                Rest()
                Duration(1680.0)
                Voice('3')
                Type('half', size='cue')
                Dot()
                Dot()
                Staff(1)
            with Note(default_x=582.42, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=511.1, default_y=-20.0, print_object='no'):
                Cue()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('3')
                Type('eighth')
                Stem('none')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-101.46)
                Staff(2)
            with Note(default_x=14.0, default_y=-291.63):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=60.16, default_y=-256.63):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.31, default_y=-236.63):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=152.47, default_y=-226.63):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=198.62, default_y=-216.63):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=244.78, default_y=-221.63):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('rit.', relative_x=2.54, relative_y=166.75, font_style='italic', font_size='11')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=290.94, default_y=-226.63):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=150.92)
                Staff(2)
            with Note(default_x=337.09, default_y=-236.63):
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
                Beam('continue', number=1)
            with Note(default_x=383.25, default_y=-246.63):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=429.4, default_y=-251.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(160.0)
                Voice('5')
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=29.8)
                Staff(2)
            with Note(default_x=487.03, default_y=-256.63):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=552.76, default_y=-291.63):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none', relative_x=6.95)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('65')
                Offset(-960.0)
                Staff(1)
                Sound(tempo=65.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('56')
                Offset(-320.0)
                Staff(1)
                Sound(tempo=56.0)
        with Measure(number='31', width=721.84):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(215.0)
                with StaffLayout(number=2):
                    StaffDistance(91.73)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=54.06, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', relative_y=53.54, font_style='italic', font_size='11')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=79.61, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=98.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=479.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=546.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=614.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=681.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(1920.0)
            with Note(default_x=98.05, default_y=5.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1440.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Stem('none')
                Staff(1)
            with Note(default_x=479.16, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=497.15, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=513.16, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=529.17, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=545.18, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('2')
                Type('16th', size='cue')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('2')
                Type('eighth', size='cue')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=98.42, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=140.72, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.03, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=225.33, default_y=-146.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=267.64, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=309.94, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-35.68)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=352.25, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=394.55, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=436.86, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=479.16, default_y=-146.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=568.99, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=658.83, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='32', width=650.91):
            with Note(default_x=17.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-78.65)
                Staff(1)
            with Note(default_x=392.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
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
                    Tuplet(type='start', bracket='yes')
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=437.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
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
            with Note(default_x=482.16, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=526.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=571.38, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=610.26, default_y=10.0):
                with Pitch():
                    Step('A')
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(print_object='no'):
                Rest()
                Duration(1440.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Staff(1)
            with Note(default_x=392.94, default_y=-5.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(15)
                    NormalNotes(8)
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
                with Notations():
                    with Tuplet(type='start', number=1, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('eighth')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('eighth')
                    with Tuplet(type='start', number=2, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(5)
                            TupletType('64th')
                        with TupletNormal():
                            TupletNumber(4)
                            TupletType('64th')
            with Note(default_x=410.59, default_y=0.0, print_object='no'):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(15)
                    NormalNotes(8)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=426.25, default_y=-5.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(15)
                    NormalNotes(8)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=441.92, default_y=0.0, print_object='no'):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(15)
                    NormalNotes(8)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=457.58, default_y=-5.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(15)
                    NormalNotes(8)
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
                with Notations():
                    Tuplet(type='stop', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(80.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(160.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(160.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Staff(1)
                with Notations():
                    Tuplet(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=17.95, default_y=-176.73):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=59.62, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=101.28, default_y=-131.73):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=142.95, default_y=-141.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=184.62, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=226.28, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-34.36)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=267.95, default_y=-171.73):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=309.61, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=351.28, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=392.94, default_y=-146.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=487.81, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=582.68, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='33', width=693.63):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(215.0)
                with StaffLayout(number=2):
                    StaffDistance(109.75)
            with Note(default_x=95.09, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-76.22)
                Staff(1)
            with Note(default_x=448.2, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
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
                    Tuplet(type='start', bracket='yes')
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=516.97, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(80.0)
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
            with Note(default_x=558.38, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(80.0)
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
            with Note(default_x=582.58, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
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
            with Note(default_x=618.25, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
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
            with Direction(placement='below'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=-101.8, relative_x=-2.45, relative_y=-9.69):
                        BeatUnit('quarter')
                        PerMinute('40')
                Staff(1)
                Sound(tempo=40.0)
            with Note(default_x=642.45, default_y=40.0):
                with Pitch():
                    Step('G')
                    Octave(6)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(print_object='no'):
                Rest()
                Duration(1440.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Staff(1)
            with Note(default_x=448.2, default_y=15.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(27.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    with Tuplet(type='start', number=1, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('eighth')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('eighth')
                    with Tuplet(type='start', number=2, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('32nd')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('32nd')
            with Note(default_x=471.47, default_y=20.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(27.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=488.02, default_y=15.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(27.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(9)
                    NormalNotes(4)
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(80.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(160.0)
                Voice('2')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(80.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Staff(1)
            with Note(default_x=670.84, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tuplet(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=95.45, default_y=-204.75):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=134.65, default_y=-179.75):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=173.84, default_y=-149.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=213.04, default_y=-159.75):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=252.23, default_y=-139.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=291.42, default_y=-144.75):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-27.75)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=330.62, default_y=-199.75):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=369.81, default_y=-179.75):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=409.01, default_y=-154.75):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=448.2, default_y=-164.75):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=558.38, default_y=-139.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=618.25, default_y=-144.75):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='34', width=679.11):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=0.57, relative_y=-36.4):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-41.22, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=24.37, default_y=-10.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=42.81, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Accent()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=29.28, relative_x=6.67, relative_y=40.0):
                        BeatUnit('quarter')
                        PerMinute('46')
                Staff(1)
                Sound(tempo=46.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-114.61)
                Staff(1)
            with Note(default_x=165.81, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=199.5, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=22.96, relative_x=6.67, relative_y=40.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=233.19, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.87, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=300.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=10.1, relative_x=6.67, relative_y=40.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=334.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=367.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=8.94)
                Staff(1)
            with Note(default_x=401.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(8)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=0.65, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.82, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=431.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=42.81, default_y=35.0, print_object='no'):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(480.0)
                Voice('2')
                Type('quarter', size='cue')
                Stem('none')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('2')
                Type('quarter', size='cue')
                Staff(1)
            with Note(default_x=431.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=42.81, default_y=-214.75):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=83.81, default_y=-179.75):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=124.81, default_y=-159.75):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=165.81, default_y=-154.75):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=259.85, default_y=-179.75):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=349.64, default_y=-149.75):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=431.53, default_y=-144.75):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=472.53, default_y=-179.75):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=513.52, default_y=-184.75):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=554.52, default_y=-179.75):
                with Pitch():
                    Step('B')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=595.52, default_y=-169.75):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=636.52, default_y=-159.75):
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('7')
                Type('quarter', size='cue')
                Staff(2)
            with Note(default_x=165.81, default_y=-154.75):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(480.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(960.0)
                Voice('7')
                Type('half', size='cue')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Offset(-160.0)
                Staff(1)
                Sound(tempo=63.0)
        with Measure(number='35', width=821.06):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(215.0)
                with StaffLayout(number=2):
                    StaffDistance(186.67)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=0.72, relative_x=-3.46, relative_y=27.88):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=79.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=33.01, relative_y=23.73):
                        BeatUnit('quarter')
                        PerMinute('56')
                Staff(1)
                Sound(tempo=56.0)
            with Note(default_x=244.39, default_y=-40.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=261.09, default_y=-35.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.79, default_y=-30.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.49, default_y=-25.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=311.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
                    Slur(type='stop', number=2)
            with Note(default_x=345.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=379.78, default_y=-20.0):
                with Pitch():
                    Step('B')
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
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=42.04, relative_x=-0.65, relative_y=21.13):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=413.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=43.24, relative_y=21.78):
                        BeatUnit('quarter')
                        PerMinute('40')
                Staff(1)
                Sound(tempo=40.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-189.26)
                Staff(1)
            with Note(default_x=515.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    with Ornaments():
                        TrillMark()
            with Note(default_x=546.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=41.93, relative_y=23.12):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=577.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=609.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=44.16, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note(default_x=640.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=671.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=702.68, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=40.41, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=733.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=765.09, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=796.29, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=83.56, default_y=-45.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('eighth', size='cue')
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=145.39, default_y=-45.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Tie(type='stop')
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('32nd')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=172.51, default_y=-40.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('32nd')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=192.83, default_y=-35.0, print_object='no'):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=213.15, default_y=-30.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=233.47, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=311.94, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=345.86, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=379.78, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter', size='cue')
                Staff(1)
            with Note(default_x=519.4, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(16)
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
                with Notations():
                    with Tuplet(type='start', number=1, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(10)
                            TupletType('32nd')
                        with TupletNormal():
                            TupletNumber(8)
                            TupletType('32nd')
                    with Tuplet(type='start', number=2, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(3)
                            TupletType('64th')
                        with TupletNormal():
                            TupletNumber(2)
                            TupletType('64th')
            with Note(default_x=535.85, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(16)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=551.52, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('64th', size='cue')
                with TimeModification():
                    ActualNotes(30)
                    NormalNotes(16)
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
                with Notations():
                    Tuplet(type='stop', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                    NormalType('32nd')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(384.0)
                Voice('2')
                Type('quarter', size='cue')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                    NormalType('32nd')
                Staff(1)
                with Notations():
                    Tuplet(type='stop', number=1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=79.61, default_y=-266.67):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=142.2, default_y=-246.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.17, default_y=-221.67):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=311.94, default_y=-231.67):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=345.86, default_y=-206.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=379.78, default_y=-211.67):
                with Pitch():
                    Step('D')
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-33.04)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.66)
                Staff(2)
            with Note(default_x=413.69, default_y=-271.67):
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=447.61, default_y=-236.67):
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
                Beam('continue', number=1)
            with Note(default_x=481.53, default_y=-211.67):
                with Pitch():
                    Step('D')
                    Octave(4)
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
            with Note(default_x=515.45, default_y=-206.67):
                with Pitch():
                    Step('E')
                    Octave(4)
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=636.56, default_y=-216.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=717.03, default_y=-236.67):
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='36', width=551.68):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=24.35, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-154.26, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=77.78)
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue262', default_y=36.17, relative_x=5.72, relative_y=68.23, font_family='MScore Text', font_size='15')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=80.0)
                Staff(1)
            with Note(default_x=145.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=498.31, default_y=-25.0):
                Grace()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=509.28, default_y=-20.0):
                Grace()
                with Pitch():
                    Step('B')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=530.87, default_y=-15.0):
                Grace()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(1920.0)
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('2')
                Type('half', size='cue')
                Staff(1)
            with Note(default_x=145.41, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(6)
                Stem('none')
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
                    with Tuplet(type='start', number=2, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(4)
                            TupletType('16th')
                        with TupletNormal():
                            TupletNumber(3)
                            TupletType('16th')
            with Note(default_x=215.58, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Ornaments():
                        TrillMark()
                        WavyLine(type='start', number=1, default_y=44.09)
            with Note(default_x=231.25, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.58, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop', number=2)
            with Note(default_x=278.24, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=293.91, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=309.57, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=325.24, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=340.91, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=356.57, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=32.14, relative_y=56.46):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=372.24, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', number=1, bracket='no', show_number='none')
            with Note(default_x=387.9, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=403.57, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=419.23, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=35.72, relative_x=1.43, relative_y=52.88):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note(default_x=434.9, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=450.57, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
            with Note(default_x=466.23, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Tuplet(type='start', number=2, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(4)
                            TupletType('16th')
                        with TupletNormal():
                            TupletNumber(3)
                            TupletType('16th')
                    with Ornaments():
                        WavyLine(type='stop', number=1, relative_x=12.99)
            with Note(default_x=481.9, default_y=-25.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=513.23, default_y=-20.0, print_object='no'):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=528.89, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('2')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop', number=1)
                    Tuplet(type='stop', number=2)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=16.16, default_y=-256.67):
                with Pitch():
                    Step('B')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=32.22, default_y=-236.67):
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
                Beam('continue', number=1)
            with Note(default_x=48.27, default_y=-211.67):
                with Pitch():
                    Step('D')
                    Octave(4)
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
            with Note(default_x=67.74, default_y=-221.67):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=87.2, default_y=-196.67):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=110.47, default_y=-201.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-37.0)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=145.77, default_y=-206.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=244.94, default_y=-211.67):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=307.6, default_y=-221.67):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=370.26, default_y=-241.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=432.92, default_y=-246.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=495.59, default_y=-276.67):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=68.6, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Offset(-160.0)
                Staff(1)
                Sound(tempo=60.0)
        with Measure(number='37', width=1008.79):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    TopSystemDistance(162.17)
                with StaffLayout(number=2):
                    StaffDistance(179.75)
            with Note(default_x=91.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Ornaments():
                        TrillMark()
                        WavyLine(type='start', number=1, default_y=124.58)
            with Note(default_x=518.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Ornaments():
                        TrillMark()
                        WavyLine(type='start', number=2, default_y=124.99)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-150.12, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=142.76, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('46')
                Staff(1)
                Sound(tempo=46.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-185.12)
                Staff(1)
            with Note(default_x=725.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(5)
                Duration(44.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(8)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=748.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(44.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(8)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=86.56, relative_x=-1.91, relative_y=76.2):
                        BeatUnit('quarter')
                        PerMinute('52')
                Staff(1)
                Sound(tempo=52.0)
            with Note(default_x=771.96, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(44.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(8)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=799.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(44.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(8)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Forward():
                Duration(1.0)
            with Note(default_x=822.39, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(44.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(8)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=849.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(6)
                Duration(44.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(8)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=73.31, relative_y=89.45):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note(default_x=872.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(44.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(8)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=895.86, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(44.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(8)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=923.25, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(44.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(8)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=69.51, relative_x=-1.27, relative_y=93.25):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=951.22, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(44.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(8)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=984.03, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(6)
                Duration(44.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(8)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(1.0)
            with Backup():
                Duration(1920.0)
            with Note(default_x=104.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=518.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=95.14, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(12)
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Tuplet(type='start', number=1, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(6)
                            TupletType('eighth')
                        with TupletNormal():
                            TupletNumber(4)
                            TupletType('eighth')
                    with Tuplet(type='start', number=2, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(4)
                            TupletType('16th')
                        with TupletNormal():
                            TupletNumber(3)
                            TupletType('16th')
            with Note(default_x=135.62, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(12)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.38, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(12)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.82, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(12)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop', number=2)
            with Note(default_x=207.57, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=224.35, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=241.12, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=257.9, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=274.67, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=291.44, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=142.76, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=308.22, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=324.99, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=341.77, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=358.54, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=375.31, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=392.09, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=408.86, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=425.63, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=442.41, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=459.18, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=475.96, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=492.73, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(40.0)
                Voice('3')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop', number=1)
                    with Ornaments():
                        WavyLine(type='stop', number=1)
            with Note(default_x=521.37, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(6)
                Stem('none')
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
                    with Tuplet(type='start', number=2, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(4)
                            TupletType('16th')
                        with TupletNormal():
                            TupletNumber(3)
                            TupletType('16th')
            with Note(default_x=543.11, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=562.86, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=595.3, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(60.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop', number=2)
            with Note(default_x=615.06, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(48.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(15)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Tuplet(type='start', number=2, bracket='no', show_number='none'):
                        with TupletActual():
                            TupletNumber(5)
                            TupletType('16th')
                        with TupletNormal():
                            TupletNumber(3)
                            TupletType('16th')
            with Note(default_x=633.18, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(48.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(15)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=664.51, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(48.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(15)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=682.62, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(48.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(15)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=700.74, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(48.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(15)
                    NormalNotes(6)
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop', number=1)
                    Tuplet(type='stop', number=2)
                    with Ornaments():
                        WavyLine(type='stop', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('3')
                Type('quarter', size='cue')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.62)
                Staff(2)
            with Note(default_x=92.01, default_y=-264.75):
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=167.41, default_y=-229.75):
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
                Beam('continue', number=1)
            with Note(default_x=236.38, default_y=-209.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=303.48, default_y=-199.75):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=370.57, default_y=-189.75):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=437.67, default_y=-194.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-35.68)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=518.61, default_y=-199.75):
                with Pitch():
                    Step('E')
                    Octave(4)
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=574.9, default_y=-209.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=644.1, default_y=-219.75):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=725.9, default_y=-229.75):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=806.41, default_y=-264.75):
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
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=902.59, default_y=-299.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=10.57)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=142.76, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Offset(-1760.0)
                Staff(1)
                Sound(tempo=63.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=60.86, relative_x=5.4, relative_y=101.9):
                        BeatUnit('quarter')
                        PerMinute('60')
                Offset(-320.0)
                Staff(1)
                Sound(tempo=60.0)
        with Measure(number='38', width=363.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-147.65, relative_x=4.11, relative_y=-42.46):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=142.76, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=15.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=102.01, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=189.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note(default_x=276.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=15.8, default_y=-284.75):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=44.54, default_y=-249.75):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=73.27, default_y=-229.75):
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
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=39.11)
                Staff(2)
            with Note(default_x=102.01, default_y=-219.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=132.47, default_y=-209.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=161.21, default_y=-214.75):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-31.72)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-81.42)
                Staff(2)
            with Note(default_x=189.94, default_y=-224.75):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=218.68, default_y=-209.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=247.41, default_y=-214.75):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=11.49)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-81.42)
                Staff(2)
            with Note(default_x=276.15, default_y=-229.75):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=304.88, default_y=-209.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=333.62, default_y=-214.75):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Offset(-160.0)
                Staff(1)
                Sound(tempo=60.0)
        with Measure(number='39', width=476.48):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(159.39)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.02, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=83.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.05, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=371.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=371.02, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=422.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=422.95, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=83.41, default_y=-249.39):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=115.37, default_y=-229.39):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=147.33, default_y=-204.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=179.28, default_y=-214.39):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=211.24, default_y=-189.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=243.19, default_y=-194.39):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-25.54)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=275.15, default_y=-249.39):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=307.11, default_y=-229.39):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=339.06, default_y=-204.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=371.02, default_y=-214.39):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=402.98, default_y=-189.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=442.92, default_y=-194.39):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-29.8)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=19.45, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Offset(-1600.0)
                Staff(1)
                Sound(tempo=69.0)
        with Measure(number='40', width=414.86):
            with Note(default_x=16.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=16.87, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-164.81)
                Staff(1)
            with Note(default_x=209.67, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
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
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=209.67, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
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
                with Notations():
                    Tied(type='stop')
            with Note(default_x=241.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=241.75, default_y=-5.0):
                Chord()
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
            with Note(default_x=273.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=273.82, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=32.69, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=305.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
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
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=305.9, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
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
            with Note(default_x=337.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=337.97, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
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
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=30.3, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(80.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Staff(1)
            with Note(default_x=390.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
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
            with Note(default_x=390.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=17.23, default_y=-244.39):
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
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=49.31, default_y=-229.39):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.38, default_y=-199.39):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=113.45, default_y=-209.39):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=145.53, default_y=-189.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=177.6, default_y=-194.39):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-25.54)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=209.67, default_y=-249.39):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=241.75, default_y=-229.39):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=273.82, default_y=-204.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=305.9, default_y=-214.39):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=337.97, default_y=-189.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=370.04, default_y=-194.39):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-31.93)
                Staff(2)
        with Measure(number='41', width=481.41):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=27.01, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-129.81, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=95.56)
            with Note(default_x=21.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=21.03, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=58.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=58.94, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=96.85, default_y=-20.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=96.85, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=134.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='stop', number=1)
            with Note(default_x=134.76, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=172.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=198.72, default_y=-25.0):
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
                    with Articulations():
                        Accent()
            with Note(default_x=210.58, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.36, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=248.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=260.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=290.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=290.26, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=24.71)
                Staff(1)
            with Note(default_x=328.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=328.17, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=366.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=366.08, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=403.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=403.99, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=441.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
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
            with Note(default_x=441.9, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-102.93)
                Staff(2)
            with Note(default_x=21.03, default_y=-264.39):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(1)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=58.94, default_y=-229.39):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.85, default_y=-194.39):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=134.76, default_y=-209.39):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=172.67, default_y=-189.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.58, default_y=-194.39):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-34.06)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-102.93)
                Staff(2)
            with Note(default_x=248.5, default_y=-249.39):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=290.26, default_y=-229.39):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=328.17, default_y=-204.39):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=366.08, default_y=-214.39):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=403.99, default_y=-189.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=441.9, default_y=-194.39):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-42.57)
                Staff(2)
        with Measure(number='42', width=526.36):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(150.99)
                with StaffLayout(number=2):
                    StaffDistance(91.73)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=75.92, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=91.65, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=91.65, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=77.42, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Staff(1)
                Sound(tempo=64.0)
            with Note(default_x=199.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=199.93, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=236.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=236.02, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=272.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(160.0)
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
            with Note(default_x=272.11, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=49.66, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=307.84, default_y=-35.0):
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
                    Slur(type='stop', number=1)
            with Note(default_x=307.84, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.4)
                Staff(2)
            with Note(default_x=91.65, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=127.75, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.84, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=199.93, default_y=-131.73):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=236.02, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=272.11, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.4)
                Staff(2)
            with Note(default_x=308.21, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=344.3, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=380.39, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=416.48, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=452.57, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=488.67, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='43', width=405.63):
            with Note(default_x=19.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=308.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=16.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1920.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Note(default_x=16.87, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1920.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=68.6)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=20.19, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=52.18, default_y=-156.73):
                with Pitch():
                    Step('C')
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
            with Note(default_x=84.16, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
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
            with Note(default_x=116.15, default_y=-156.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=148.14, default_y=-151.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=180.12, default_y=-156.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=212.11, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=244.1, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=276.08, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=308.07, default_y=-141.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=340.06, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=372.04, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='44', width=440.75):
            with Note(default_x=12.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=225.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=332.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=12.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=12.36, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=225.58, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=225.58, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=12.72, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=48.26, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.79, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=119.33, default_y=-146.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=154.87, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=190.4, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=225.94, default_y=-131.73):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=261.47, default_y=-136.73):
                with Pitch():
                    Step('G')
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
            with Note(default_x=297.01, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Note(default_x=332.55, default_y=-166.73):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(160.0)
                Voice('5')
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
            with Note(default_x=368.08, default_y=-171.73):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=403.62, default_y=-201.73):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=4.12)
                Staff(2)
        with Measure(number='45', width=518.59):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(91.73)
            with Note(default_x=83.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=278.13, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=289.09, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=313.01, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=414.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=83.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=83.05, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=312.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=300.06, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=312.65, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(960.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(1920.0)
            with Note(default_x=83.05, default_y=5.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(720.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
                Notehead('normal', filled='no')
                Staff(1)
            with Note(default_x=247.63, default_y=0.0, print_object='no'):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(120.0)
                Voice('3')
                Type('16th', size='cue')
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=287.83, default_y=-5.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(120.0)
                Voice('3')
                Type('16th', size='cue')
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('3')
                Type('half', size='cue')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=83.41, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=117.15, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.88, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=184.62, default_y=-136.73):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=218.35, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=267.42, default_y=-126.73):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-25.54)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=313.01, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=346.74, default_y=-166.73):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=380.48, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=414.21, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=449.52, default_y=-201.73):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=483.26, default_y=-196.73):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-31.93)
                Staff(2)
        with Measure(number='46', width=366.87):
            with Note(default_x=17.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=17.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=17.59, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1440.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=17.95, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=46.81, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=75.67, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=105.56, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=134.42, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=163.28, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-27.75)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=192.13, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=220.99, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=249.85, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=278.7, default_y=-136.73):
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=307.56, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=336.42, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='47', width=487.28):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=17.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=17.59, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=222.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=222.41, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(print_object='no'):
                Rest()
                Duration(1440.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Staff(1)
            with Note(default_x=415.66, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=415.66, default_y=-5.0):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=327.15, default_y=-15.0, print_object='no'):
                Cue()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('none')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(960.0)
                Voice('3')
                Type('half', size='cue')
                Staff(1)
            with Note(default_x=222.41, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=222.41, default_y=0.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=327.15, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(320.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=327.15, default_y=0.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(320.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=443.15, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Tie(type='stop')
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=443.15, default_y=0.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Tie(type='stop')
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=464.49, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(80.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=464.49, default_y=-5.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(80.0)
                Voice('3')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=17.95, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=52.09, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=86.22, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=120.36, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=154.5, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=188.63, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-22.47)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-97.2)
                Staff(2)
            with Note(default_x=222.77, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=256.9, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=291.04, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=325.18, default_y=-136.73):
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=383.18, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=441.18, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='48', width=494.14):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(91.73)
            with Note(default_x=91.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=91.65, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=392.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=392.5, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=91.65, default_y=-15.0, print_object='no'):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('none')
                Staff(1)
            with Note(default_x=91.65, default_y=-5.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1440.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('none')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(480.0)
                Voice('3')
                Type('quarter', size='cue')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.19)
                Staff(2)
            with Note(default_x=92.01, default_y=-181.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=125.36, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Note(default_x=159.06, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=192.41, default_y=-131.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=225.76, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=259.1, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-27.75)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.19)
                Staff(2)
            with Note(default_x=292.45, default_y=-181.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=325.8, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Note(default_x=359.15, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
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
            with Note(default_x=392.5, default_y=-131.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=425.84, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=459.19, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='49', width=474.36):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=17.23, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=182.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=182.47, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=-2.91, relative_y=69.08):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=240.53, default_y=0.0):
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
            with Note(default_x=240.53, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=298.58, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=298.58, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=2.74, relative_y=63.8):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note(default_x=356.64, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=356.64, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=414.7, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=414.7, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(print_object='no'):
                Rest()
                Duration(1440.0)
                Voice('2')
                Type('half', size='cue')
                Dot()
                Staff(1)
            with Note(default_x=356.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.18)
                Staff(2)
            with Note(default_x=17.23, default_y=-181.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=52.96, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Note(default_x=88.69, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=124.41, default_y=-131.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=160.14, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=204.8, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-31.72)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.16)
                Staff(2)
            with Note(default_x=240.53, default_y=-181.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=280.72, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Note(default_x=320.91, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
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
            with Note(default_x=356.64, default_y=-131.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=396.84, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=437.03, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='50', width=404.25):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=-3.28, relative_y=64.62):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=61.11)
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=26.25, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=112.51, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=112.51, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=7.5, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note():
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=15.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(960.0)
                Voice('2')
                Type('half', size='cue')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=53.68)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-102.93)
                Staff(2)
            with Note(default_x=15.8, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=48.04, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=80.27, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=112.51, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=144.75, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=176.99, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-23.79)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-102.93)
                Staff(2)
            with Note(default_x=209.22, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=241.46, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=273.7, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=305.94, default_y=-136.73):
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=338.17, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=370.41, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='51', width=489.0):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    TopSystemDistance(85.05)
                with StaffLayout(number=2):
                    StaffDistance(94.68)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=56.73, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=91.65, default_y=-5.0):
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=91.65, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.44, relative_y=-40.0):
                        OtherDynamics('(')
                        P()
                        OtherDynamics(')')
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=188.57, default_y=-5.0):
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
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=188.57, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=220.88, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=220.88, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=253.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(160.0)
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
            with Note(default_x=253.18, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=70.95, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=285.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=337.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=29.02, relative_y=58.5):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note(default_x=390.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=390.48, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=422.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=422.79, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=455.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(160.0)
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
            with Note(default_x=455.1, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note():
                Rest()
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=188.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=390.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(960.0)
                Voice('3')
                Type('half', size='cue')
                Staff(1)
            with Note(default_x=285.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=390.48, default_y=-10.0, print_object='no'):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('3')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.0)
                Staff(2)
            with Note(default_x=91.65, default_y=-184.68):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=123.96, default_y=-164.68):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=156.27, default_y=-129.68):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=188.57, default_y=-139.68):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=220.88, default_y=-144.68):
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
                Beam('continue', number=1)
            with Note(default_x=253.18, default_y=-149.68):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-29.08)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.0)
                Staff(2)
            with Note(default_x=285.49, default_y=-184.68):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=317.8, default_y=-164.68):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=358.18, default_y=-129.68):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=390.48, default_y=-139.68):
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=422.79, default_y=-144.68):
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
                Beam('continue', number=1)
            with Note(default_x=455.1, default_y=-149.68):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='52', width=420.63):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=39.99, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=7.0, default_y=0.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=30.44, default_y=-5.0):
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
            with Note():
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=30.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=30.44, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(960.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(960.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=33.93, default_y=0.0, print_object='no'):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(160.0)
                Voice('3')
                Type('eighth', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=67.77, default_y=-5.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(320.0)
                Tie(type='start')
                Voice('3')
                Type('quarter', size='cue')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='stop')
            with Note(default_x=133.7, default_y=-5.0, print_object='no'):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('3')
                Type('quarter', size='cue')
                Stem('none')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(960.0)
                Voice('3')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.19)
                Staff(2)
            with Note(default_x=30.8, default_y=-184.68):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=63.03, default_y=-149.68):
                with Pitch():
                    Step('E')
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
            with Note(default_x=96.73, default_y=-124.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=128.96, default_y=-134.68):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=161.19, default_y=-144.68):
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
                Beam('continue', number=1)
            with Note(default_x=193.42, default_y=-149.68):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-26.43)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.19)
                Staff(2)
            with Note(default_x=225.65, default_y=-184.68):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=257.88, default_y=-149.68):
                with Pitch():
                    Step('E')
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
            with Note(default_x=290.11, default_y=-124.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
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
            with Note(default_x=322.34, default_y=-134.68):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=354.57, default_y=-144.68):
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
                Beam('continue', number=1)
            with Note(default_x=386.8, default_y=-149.68):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='53', width=463.11):
            with Note(default_x=15.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(1920.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=35.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(720.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=35.85, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(720.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=179.11, default_y=-30.0):
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
            with Note(default_x=179.11, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.12, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=235.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=235.59, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=292.07, default_y=-30.0):
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
            with Note(default_x=292.07, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.2, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note(default_x=348.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=348.55, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=405.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=405.03, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.18)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=45.15)
                Staff(2)
            with Note(default_x=18.36, default_y=-184.68):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=53.12, default_y=-149.68):
                with Pitch():
                    Step('E')
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
            with Note(default_x=87.87, default_y=-124.68):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=122.63, default_y=-134.68):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=157.39, default_y=-144.68):
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
                Beam('continue', number=1)
            with Note(default_x=200.83, default_y=-149.68):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-51.54)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.17)
                Staff(2)
            with Note(default_x=235.59, default_y=-184.68):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=274.69, default_y=-149.68):
                with Pitch():
                    Step('E')
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
            with Note(default_x=313.79, default_y=-124.68):
                with Pitch():
                    Step('C')
                    Octave(4)
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
            with Note(default_x=348.55, default_y=-134.68):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=387.65, default_y=-144.68):
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
                Beam('continue', number=1)
            with Note(default_x=426.75, default_y=-149.68):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='54', width=449.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.66)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(91.73)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=15.84, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=51.11)
            with Note(default_x=91.65, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Note(default_x=91.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=91.65, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1440.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.0)
                Staff(2)
            with Note(default_x=92.01, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=121.69, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.37, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=181.26, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=210.94, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=240.62, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-29.08)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.0)
                Staff(2)
            with Note(default_x=270.29, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=299.97, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=329.65, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=359.32, default_y=-136.73):
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=389.0, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=418.67, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='55', width=367.21):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=40.0)
            with Note(default_x=16.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=16.87, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1440.0)
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
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=278.52, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=278.52, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=278.52, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-106.22)
                Staff(2)
            with Note(default_x=17.23, default_y=-181.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=46.26, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Note(default_x=75.29, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
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
            with Note(default_x=104.33, default_y=-131.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=133.36, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=162.39, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Note(default_x=191.42, default_y=-181.73):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=220.45, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Note(default_x=249.48, default_y=-121.73):
                with Pitch():
                    Step('C')
                    Octave(4)
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
            with Direction(placement='above'):
                with DirectionType():
                    Words('ca', relative_y=60.0, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=278.52, default_y=-131.73):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=45.0)
                Staff(2)
            with Note(default_x=307.55, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=336.58, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='56', width=361.76):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=17.23, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('50')
                Staff(1)
                Sound(tempo=50.0)
            with Note():
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.0)
                Staff(2)
            with Note(default_x=17.23, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=45.05, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=72.87, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('lan', relative_y=60.0, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=102.76, default_y=-136.73):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=45.0)
                Staff(2)
            with Note(default_x=130.58, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=158.4, default_y=-146.73):
                with Pitch():
                    Step('E')
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
            with Note(default_x=186.21, default_y=-181.73):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=214.03, default_y=-161.73):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=241.85, default_y=-126.73):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(160.0)
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('do', relative_y=60.0, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=269.67, default_y=-136.73):
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=297.48, default_y=-141.73):
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
                Beam('continue', number=1)
            with Note(default_x=325.3, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(160.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('40')
                Offset(-480.0)
                Staff(1)
                Sound(tempo=40.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('30')
                Offset(-320.0)
                Staff(1)
                Sound(tempo=30.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.58, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('20')
                Offset(-160.0)
                Staff(1)
                Sound(tempo=20.0)
        with Measure(number='57', width=193.82):
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=3.58, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('30')
                Staff(1)
                Sound(tempo=30.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=21.39, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.22)
                Staff(2)
            with Note(default_x=21.39, default_y=-146.73):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1440.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    with Articulations():
                        Accent()
            with Note(default_x=21.39, default_y=-136.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1440.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=21.39, default_y=-111.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1440.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')