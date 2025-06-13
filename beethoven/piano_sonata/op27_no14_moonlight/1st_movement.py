with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Moonlight Sonata I')
    with Identification():
        Creator('Ludwig van Beethoven', type='composer')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(7.04)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1687.5)
            PageWidth(1193.18)
            with PageMargins(type='both'):
                LeftMargin(45.4545)
                RightMargin(45.4545)
                TopMargin(28.4091)
                BottomMargin(85.2273)
        WordFont(font_family='Calibri', font_size='8')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Moonlight Sonata I', default_x=596.59, default_y=1659.09, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Ludwig van Beethoven', default_x=1147.73, default_y=1559.09, justify='right', valign='bottom', font_size='10')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Sonata no.14 Op.27', default_x=596.59, default_y=1612.56, justify='center', valign='top', font_size='12')
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
        with Measure(number='1', width=437.94):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    TopSystemDistance(200.0)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(4)
                with Time():
                    Beats('4')
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
                    Words('\ueca5', default_x=-43.12, relative_y=20.0, font_family='Gootville Text', font_size='6')
                    Words(' = ', font_weight='bold', font_family='Calibri')
                Staff(1)
                Sound(tempo=450.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-43.12, default_y=18.23, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('45')
                Staff(1)
                Sound(tempo=45.0)
            with Direction():
                with DirectionType():
                    Words('Adagio Sostenuto', default_y=1.34, relative_y=20.0)
                Staff(1)
            with Note(default_x=135.12, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=161.25, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=185.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=210.57, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=236.71, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=261.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=286.03, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=312.17, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=336.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=361.49, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=387.63, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=412.28, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('sempre pp e senza sordino', relative_y=40.0)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=132.36, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=132.36, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='2', width=320.59):
            with Note(default_x=17.76, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=43.9, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=93.22, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=119.36, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=144.01, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=168.67, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=194.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=219.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=244.13, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=270.27, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=294.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='3', width=325.9):
            with Note(default_x=15.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=41.14, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=65.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=90.46, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=116.59, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=141.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=165.91, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=196.09, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=220.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=245.41, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=275.58, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=300.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.0, default_y=-175.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=165.91, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=165.91, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='4', width=438.61):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(99.34)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Note(default_x=112.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=149.57, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=174.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=199.12, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=225.26, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=250.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=274.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=300.94, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=325.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=350.49, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=388.06, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=412.84, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=112.0, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=274.8, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=274.8, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='5', width=333.16):
            with Note(default_x=17.76, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=42.41, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.06, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=91.71, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=117.85, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.5, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=167.15, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=193.29, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=217.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=242.59, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=268.73, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=293.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=242.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=309.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='6', width=312.67):
            with Note(default_x=21.2, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=45.63, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.17, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=90.71, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=113.24, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=135.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=158.31, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=180.85, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=203.39, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=225.92, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=250.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=272.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=21.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=225.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=289.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=18.44, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
            with Note(default_x=18.44, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=18.44, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='7', width=423.56):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(99.34)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Note(default_x=112.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=138.13, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=189.64, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=215.77, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=241.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=267.28, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=293.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=319.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=344.92, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=371.05, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=396.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=112.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=267.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=112.0, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=267.28, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=267.28, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='8', width=331.56):
            with Note(default_x=15.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=41.3, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=67.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=93.89, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=120.19, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=146.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=172.78, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=199.08, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=225.37, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=251.67, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=277.97, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=304.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=15.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=172.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=251.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.0, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=172.78, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=172.78, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='9', width=329.32):
            with Note(default_x=17.76, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=43.9, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=69.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=95.4, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=121.54, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=147.29, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=173.04, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=199.18, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=224.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=250.68, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=276.82, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=302.57, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=17.76, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='10', width=427.84):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(99.34)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Note(default_x=114.76, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=140.9, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=164.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=188.09, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=214.23, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=237.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=261.42, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=287.56, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=311.15, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=338.33, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=364.47, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=388.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=338.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=404.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=112.0, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='11', width=326.88):
            with Note(default_x=18.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=44.94, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=72.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
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
            with Note(default_x=94.87, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=121.01, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=143.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=166.54, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=192.68, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=215.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=238.2, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=264.34, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=287.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=18.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=238.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=303.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=16.04, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
            with Note(default_x=16.04, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='12', width=329.72):
            with Note(default_x=18.04, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=58.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=81.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=103.57, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=129.71, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=152.24, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=174.77, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=212.35, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=234.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=257.41, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=283.55, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=306.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=18.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=257.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=18.04, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=18.04, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=103.57, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=103.57, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=174.77, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=174.77, default_y=-175.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='13', width=448.29):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(99.34)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Note(default_x=112.0, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=139.29, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
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
            with Note(default_x=196.76, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=224.05, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=251.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=283.52, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=310.82, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=338.11, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=365.41, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=392.7, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=419.99, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=112.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=283.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=365.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=112.0, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=283.52, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=365.41, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='14', width=351.69):
            with Note(default_x=15.0, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=41.79, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=71.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
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
            with Note(default_x=98.76, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=125.56, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=152.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=179.15, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=216.72, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=243.52, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=270.31, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=297.1, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=323.9, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=15.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=179.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=179.15, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=179.15, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='15', width=284.45):
            with Note(default_x=17.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=47.94, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=67.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=87.37, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=108.51, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=128.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=147.95, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=180.52, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=200.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=219.96, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=241.1, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=260.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=17.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(24.0)
            with Note(default_x=219.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=15.0, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='16', width=436.73):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-102.64)
                Staff(1)
            with Note(default_x=116.03, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=142.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
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
            with Note(default_x=195.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=222.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=248.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-102.64)
                Staff(1)
            with Note(default_x=274.68, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=300.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=327.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=356.84, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=383.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=409.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=116.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=356.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=116.03, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=116.03, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=195.8, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=195.8, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=274.68, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=274.68, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=356.84, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=356.84, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='17', width=313.98):
            with Note(default_x=17.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=42.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=91.57, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=116.17, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=140.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=165.37, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=189.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=214.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=239.17, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=263.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=288.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=17.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=239.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=15.0, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='18', width=333.73):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-102.64)
                Staff(1)
            with Note(default_x=13.04, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=39.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
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
            with Note(default_x=92.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=119.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=145.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-102.64)
                Staff(1)
            with Note(default_x=171.68, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=197.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=224.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=253.85, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=280.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=306.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=253.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.04, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.04, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=92.8, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=92.8, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=171.68, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=171.68, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=253.85, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=253.85, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='19', width=403.14):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(115.76)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Note(default_x=112.0, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=135.04, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=158.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=181.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=204.16, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=227.19, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=250.23, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=280.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=309.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=333.02, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=356.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=379.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=112.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=250.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=112.0, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=250.23, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=250.23, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='20', width=329.11):
            with Note(default_x=20.44, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=46.58, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=71.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=97.36, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=123.49, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=174.27, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=200.41, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=225.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=251.19, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=277.33, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=302.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=20.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=174.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=20.44, default_y=-225.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=20.44, default_y=-190.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=174.27, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=174.27, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='21', width=352.18):
            with Note(default_x=18.04, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=44.39, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=74.56, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
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
            with Note(default_x=100.91, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=127.26, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=153.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=179.96, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=206.3, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=238.88, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=265.23, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=291.58, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=317.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=18.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=179.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=18.04, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=18.04, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=179.96, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=179.96, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='22', width=396.36):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(118.1)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
            with Note(default_x=112.0, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=135.07, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=158.14, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=181.21, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=204.28, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=227.36, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=250.43, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=273.5, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=296.57, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=319.64, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=349.22, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=372.29, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=112.0, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=250.43, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=319.64, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=250.43, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='23', width=353.22):
            with Note(default_x=17.76, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=43.13, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.5, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Note(default_x=109.73, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=135.86, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=161.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=186.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=211.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=237.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=262.7, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=288.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=313.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=17.76, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(24.0)
            with Note(default_x=262.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=329.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-200.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='24', width=334.86):
            with Note(default_x=21.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=46.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=71.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=95.89, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=120.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=145.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=170.59, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=195.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=220.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=245.29, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=270.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=295.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=21.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=245.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=311.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=18.44, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
            with Note(default_x=18.44, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=18.44, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='25', width=354.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(115.76)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Note(default_x=112.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=133.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=149.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-97.64)
                Staff(1)
            with Note(default_x=166.52, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=187.66, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=204.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=238.93, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=260.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=276.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=293.45, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=314.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=331.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=112.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=238.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=293.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=112.0, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=238.93, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=238.93, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=293.45, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=293.45, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='26', width=233.22):
            with Note(default_x=20.44, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=44.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=61.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=77.81, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=94.29, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=110.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=127.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=143.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=160.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=176.64, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=193.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=20.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=176.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=20.44, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(1)
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=20.44, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=20.44, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=176.64, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=176.64, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=176.64, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='27', width=237.93):
            with Note(default_x=15.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=31.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=48.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=64.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=81.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=97.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-95.06)
                Staff(1)
            with Note(default_x=114.05, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=130.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=147.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=163.58, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=184.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=214.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=15.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=114.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=163.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.0, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.0, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=114.05, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=114.05, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=163.58, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=163.58, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='28', width=258.36):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.32, default_y=-41.33, relative_x=3.46, relative_y=-58.73):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=15.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=50.01, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=71.15, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=87.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=104.54, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=125.68, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=142.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=159.06, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=180.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=196.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=213.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=234.73, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=87.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=142.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=196.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=12.68, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=12.68, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='29', width=358.26):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(115.76)
                with StaffLayout(number=2):
                    StaffDistance(181.97)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=144.93, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=166.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-204.66)
                Staff(1)
            with Note(default_x=183.59, default_y=-226.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=201.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=222.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=239.78, default_y=-221.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
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
                    Wedge(type='stop', number=1, relative_x=-2.26)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-204.66)
                Staff(1)
            with Note(default_x=257.3, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=278.44, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=295.97, default_y=-231.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
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
                    Wedge(type='stop', number=1, relative_x=4.52)
                Staff(1)
            with Note(default_x=313.49, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=334.63, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=183.59, default_y=-226.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=239.78, default_y=-221.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=295.97, default_y=-231.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-296.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=112.0, default_y=-261.97):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='30', width=227.23):
            with Note(default_x=17.76, default_y=-236.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=34.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=51.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-100.63)
                Staff(1)
            with Note(default_x=68.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=85.34, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=102.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=119.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-1.51)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-100.63)
                Staff(1)
            with Note(default_x=136.02, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=152.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=169.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=0.75)
                Staff(1)
            with Note(default_x=186.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=203.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=68.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=119.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=169.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-296.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-261.97):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='31', width=232.75):
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(0)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=39.42, default_y=-236.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=56.39, default_y=-226.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
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
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=73.36, default_y=-211.97):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=90.33, default_y=-236.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=107.3, default_y=-226.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=124.27, default_y=-201.97):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
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
                    Wedge(type='stop', number=1, relative_x=-2.26)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=141.24, default_y=-236.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.21, default_y=-226.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=175.18, default_y=-211.97):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
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
                    Wedge(type='stop', number=1, relative_x=5.28)
                Staff(1)
            with Note(default_x=192.14, default_y=-236.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=209.11, default_y=-226.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(48.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=73.36, default_y=-211.97):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=124.27, default_y=-201.97):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=175.18, default_y=-211.97):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-296.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-261.97):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='32', width=266.19):
            with Direction(placement='below'):
                with DirectionType():
                    Words('poco cresc.', default_y=-40.0, relative_x=-0.75, relative_y=-45.14, font_size='9')
                Staff(1)
            with Note(default_x=17.76, default_y=-241.97):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=39.42, default_y=-221.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=56.94, default_y=-231.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=74.47, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=100.61, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=121.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=142.88, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=160.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=177.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=195.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=212.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=242.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-296.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-261.97):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='33', width=389.14):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Note(default_x=114.76, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=137.54, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.32, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=183.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=205.88, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=228.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=251.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=274.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=297.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=319.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=342.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=365.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=112.0, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='34', width=348.09):
            with Note(default_x=17.76, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=48.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=74.11, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=103.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=129.1, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=154.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=179.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=205.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=230.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=261.69, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=287.1, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=321.67, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='35', width=347.21):
            with Note(default_x=15.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=45.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=72.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=98.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=125.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=152.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=178.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=205.21, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=231.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=266.39, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=293.0, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=319.6, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
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
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=12.68, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=12.68, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='36', width=408.03):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(136.84)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Note(default_x=123.43, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=146.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.62, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=192.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=215.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=245.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=268.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=291.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=314.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=337.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=360.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=383.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=120.67, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=120.67, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='37', width=358.54):
            with Note(default_x=17.76, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=52.34, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=77.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
            with Note(default_x=126.41, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=155.99, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=181.18, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=206.38, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=231.57, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=256.76, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=281.96, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=307.15, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=332.35, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
                Duration(48.0)
            with Forward():
                Duration(24.0)
            with Note(default_x=206.38, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=231.57, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=281.96, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.0, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='38', width=317.87):
            with Note(default_x=15.44, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=62.85, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=85.94, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=109.04, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=132.13, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=155.22, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=178.31, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=201.41, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=224.5, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=247.59, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=270.68, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=293.78, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=31.08, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=178.31, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=247.59, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=12.68, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=12.68, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='39', width=443.59):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(136.84)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Note(default_x=118.43, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=165.85, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=190.8, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=215.76, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=240.72, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=265.68, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=292.85, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=317.81, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=342.76, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=367.72, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=392.68, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=417.64, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=134.07, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=292.85, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=367.72, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=115.67, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=115.67, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='40', width=329.56):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-95.0)
                Staff(1)
            with Note(default_x=15.44, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=62.85, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=87.01, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=111.16, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=135.32, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=159.47, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=183.63, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=207.78, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=231.94, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=256.09, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=280.25, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=304.4, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=31.07, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.44, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.44, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=183.63, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=183.63, default_y=-175.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='41', width=311.28):
            with Note(default_x=15.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=39.16, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=63.31, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=87.47, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=111.62, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=135.78, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=159.93, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=184.09, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=213.66, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=237.82, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=261.97, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=286.13, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.0, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=159.93, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=159.93, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='42', width=445.83):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(136.84)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.16, default_y=-40.0, relative_x=6.06, relative_y=-52.27):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=114.76, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=139.28, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.8, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Note(default_x=205.03, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=231.17, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=255.69, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=280.21, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=306.35, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=330.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=355.39, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=381.53, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=406.05, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=355.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=422.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=112.0, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=112.0, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='43', width=313.77):
            with Note(default_x=21.2, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=45.63, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.29, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=90.95, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=113.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=136.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=158.93, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=181.58, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=204.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=226.9, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=251.34, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=273.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=21.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=226.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=290.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=18.44, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
            with Note(default_x=18.44, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=18.44, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='44', width=324.84):
            with Note(default_x=15.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=41.14, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=92.21, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=118.35, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=143.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=169.42, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=195.56, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=221.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=246.63, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=272.77, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=298.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=15.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=169.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.0, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=169.42, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=169.42, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='45', width=436.91):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(-0.0)
                    SystemDistance(136.84)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Note(default_x=112.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=138.99, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=192.98, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=219.97, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=246.96, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=273.96, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=300.95, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=327.94, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=354.93, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=381.93, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=408.92, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=112.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=273.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=354.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=112.0, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=273.96, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=273.96, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='46', width=327.11):
            with Note(default_x=17.76, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=43.9, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=92.57, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=116.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=141.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=165.57, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=189.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=214.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=238.57, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=263.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=287.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=17.76, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(24.0)
            with Note(default_x=238.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=303.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='47', width=320.41):
            with Note(default_x=17.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=42.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=65.97, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=89.75, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=113.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=137.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=161.09, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=184.86, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=208.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=232.42, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=256.86, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=280.63, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=17.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=232.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=296.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='48', width=355.33):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-106.06)
                Staff(1)
            with Note(default_x=112.0, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=133.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=149.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=166.66, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=187.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=204.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-106.06)
                Staff(1)
            with Note(default_x=239.13, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=260.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=277.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=293.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=314.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=331.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=112.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=239.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=293.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=112.0, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=239.13, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=239.13, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=293.8, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=293.8, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='49', width=225.34):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.16, default_y=-52.06, relative_x=3.16, relative_y=-59.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=20.44, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=36.92, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=53.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=69.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=86.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=102.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=119.31, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=135.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=152.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=168.74, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=185.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=201.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=20.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=119.31, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=20.44, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=20.44, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=20.44, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=119.31, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=119.31, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=119.31, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='50', width=246.37):
            with Note(default_x=13.04, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=29.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=46.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=62.86, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=79.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=96.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=130.64, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=151.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=168.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=184.99, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=206.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=222.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=13.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=130.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=13.04, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=13.04, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=130.64, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=130.64, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='51', width=257.39):
            with Note(default_x=17.76, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=42.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=58.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=75.54, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=96.68, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=113.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=130.02, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=162.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=179.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=195.95, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=217.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=233.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=17.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=195.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=15.0, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='52', width=418.52):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(-0.0)
                    SystemDistance(136.84)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-95.35)
                Staff(1)
            with Note(default_x=116.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=140.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=190.19, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=214.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=239.63, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-95.35)
                Staff(1)
            with Note(default_x=264.35, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=289.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=313.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=343.36, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=368.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=392.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=116.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=343.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=116.03, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=116.03, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=190.19, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=190.19, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=264.35, default_y=-175.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=264.35, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=343.36, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=343.36, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='53', width=320.25):
            with Note(default_x=17.76, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=55.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=79.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=103.56, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=127.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=151.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=175.46, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=199.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=223.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=247.35, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=271.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=295.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=17.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=247.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=15.0, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='54', width=345.67):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-105.53)
                Staff(1)
            with Note(default_x=13.04, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=40.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=67.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=95.42, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=122.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=150.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-105.53)
                Staff(1)
            with Note(default_x=177.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=205.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=232.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=262.29, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=289.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=317.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=262.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.04, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.04, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=95.42, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=95.42, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=177.8, default_y=-175.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=177.8, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=262.29, default_y=-185.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=262.29, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='55', width=387.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(136.84)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Note(default_x=112.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=144.57, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=166.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=188.39, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=210.3, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=232.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=254.13, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=276.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=297.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=319.86, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=341.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=363.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=112.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=254.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=112.0, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=254.13, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=254.13, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='56', width=284.4):
            with Note(default_x=18.04, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=42.47, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=64.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=86.13, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=107.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=151.62, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=173.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=195.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=217.11, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=238.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=260.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=18.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(36.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=217.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=18.04, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=18.04, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=217.11, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=217.11, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='57', width=412.71):
            with Note(default_x=15.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=48.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=81.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=114.18, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=147.24, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=180.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=213.36, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=246.42, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=279.48, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=312.53, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=345.59, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=378.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=15.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=114.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=213.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=312.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=15.0, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=114.18, default_y=-195.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=114.18, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=213.36, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=213.36, default_y=-170.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=312.53, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=312.53, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='58', width=569.12):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(136.84)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-117.01)
                Staff(1)
            with Note(default_x=112.0, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=150.01, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=188.02, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=226.03, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=264.04, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=302.05, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=340.06, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=378.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=416.08, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-117.01)
                Staff(1)
            with Note(default_x=454.09, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=492.1, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=530.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=1.0)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=112.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=340.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=454.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=112.0, default_y=-175.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=340.06, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=340.06, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=454.09, default_y=-220.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=454.09, default_y=-185.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='59', width=515.31):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.16, default_y=-50.01, relative_x=5.63, relative_y=-72.01):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=15.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=56.61, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=98.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=139.83, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=181.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=223.05, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=264.66, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=306.27, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=347.88, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=389.49, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=431.1, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=472.7, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=15.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=264.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=15.0, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=264.66, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=264.66, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='60', width=472.66):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(136.84)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Note(default_x=114.76, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=143.43, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=172.09, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=200.76, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=229.43, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=258.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=286.76, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=315.43, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=344.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=372.77, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=401.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=430.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Note(default_x=114.76, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.32, relative_y=20.2):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note(default_x=117.52, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=372.77, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(9.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=446.24, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='61', width=318.6):
            with Note(default_x=21.2, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=44.62, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=91.46, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=114.88, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=138.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=161.72, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=185.15, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=208.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=231.99, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=255.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=278.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=18.44, default_y=-205.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note(default_x=23.96, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=231.99, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(9.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=294.97, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='62', width=293.17):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-95.95)
                Staff(1)
            with Note(default_x=17.76, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=39.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=60.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=82.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=103.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=124.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=146.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=167.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=189.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=210.55, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=231.97, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=253.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note(default_x=20.52, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=210.55, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(9.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=269.53, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='63', width=444.02):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    TopSystemDistance(50.0)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-97.11)
                Staff(1)
            with Note(default_x=118.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=138.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=159.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=179.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=199.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=220.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
            with Note(default_x=268.89, default_y=15.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=295.03, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=315.35, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='stop')
            with Note(default_x=356.36, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=383.93, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=404.25, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=344.92, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=115.67, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note(default_x=121.2, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=344.92, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(9.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=420.39, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='64', width=299.38):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-97.11)
                Staff(1)
            with Note(default_x=17.76, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=17.76, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=43.9, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Note(default_x=85.13, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=104.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=123.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=143.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=162.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=182.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=201.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=220.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=240.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=259.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note(default_x=20.52, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=220.83, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(9.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=275.75, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='65', width=341.03):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-96.01)
                Staff(1)
            with Note(default_x=15.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=35.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=56.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=76.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=96.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=117.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
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
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
            with Note(default_x=165.9, default_y=15.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=192.03, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=212.35, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='stop')
            with Note(default_x=253.36, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=280.94, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=301.25, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(48.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=241.92, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=12.68, default_y=-215.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note(default_x=18.2, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=241.92, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(9.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=317.39, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(3.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='66', width=418.31):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(17.84)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(100.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-95.83)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-95.83)
                Staff(1)
            with Note(default_x=114.76, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=114.76, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=139.79, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Note(default_x=164.81, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=190.95, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=217.09, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=242.12, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=292.17, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=317.2, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=342.23, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=367.26, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=392.28, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
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
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=112.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(48.0)
            with Note(default_x=117.52, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=267.14, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='67', width=301.31):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=41.31, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=64.85, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=88.4, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=111.95, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=135.49, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
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
            with Note(default_x=159.04, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=182.58, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=206.13, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=229.68, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=253.22, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=276.77, default_y=-190.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
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
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note(default_x=20.52, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(24.0)
        with Measure(number='68', width=182.4):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(default_x=98.2, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=98.2, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=98.2, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.32, relative_x=13.62, relative_y=47.05):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=98.2, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=98.2, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=98.2, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='69', width=182.4):
            with Note(default_x=15.0, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', default_y=9.4, relative_y=10.0)
            with Note(default_x=15.0, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=15.0, default_y=10.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-115.0)
                Staff(2)
            with Note(default_x=15.0, default_y=-200.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=15.0, default_y=-180.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=15.0, default_y=-165.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')