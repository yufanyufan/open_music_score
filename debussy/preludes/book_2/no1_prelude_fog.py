with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Brouillards')
    with Identification():
        Creator('Claude Debussy (1862-1918)', type='composer')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(5.6)
            Tenths(40.0)
        with PageLayout():
            PageHeight(2120.94)
            PageWidth(1500.43)
            with PageMargins(type='even'):
                LeftMargin(71.4286)
                RightMargin(71.4286)
                TopMargin(71.4286)
                BottomMargin(142.857)
            with PageMargins(type='odd'):
                LeftMargin(71.4286)
                RightMargin(71.4286)
                TopMargin(71.4286)
                BottomMargin(142.857)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Brouillards', default_x=750.214, default_y=2049.51, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('(Fog)\n', default_x=750.214, default_y=1978.08, justify='center', valign='top', font_size='14')
        CreditWords('\n')
        CreditWords('No 1 from Préludes Book 2\n')
        CreditWords(None)
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Claude Debussy\n', default_x=1429.0, default_y=1885.22, justify='right', valign='bottom', font_size='12')
        CreditWords('(1862-1918)\n')
        CreditWords(None)
    with PartList():
        with ScorePart(id='P1'):
            PartName('Grand Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=1336.92):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    TopSystemDistance(300.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(-145.0)
            with Attributes():
                Divisions(240.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('4')
                    BeatType('8')
                Staves(3)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('G')
                    Line(2)
                with Clef(number=3):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Modéré ', default_x=-39.8, default_y=81.6, relative_y=20.0, font_weight='bold', font_size='12')
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-39.8, default_y=81.6, relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('88')
                Staff(1)
                Sound(tempo=44.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('la m.g. un peu en valeur sur la m.d.', relative_y=50.27, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('extrêmement égal et léger', default_y=56.94, relative_y=20.0, font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-22.34, relative_y=-44.69):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=86.23, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=148.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=211.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=273.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=336.05, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=398.5, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=460.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=523.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=585.86, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=648.32, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=710.77, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=773.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=835.68, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=898.14, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=960.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=1023.04, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=1085.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1147.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1210.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1272.86, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('una corda', default_y=-141.34, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-153.21)
                Staff(2)
            with Note(default_x=86.23, default_y=-155.0):
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
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=86.23, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=86.23, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
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
                    Pedal(type='start', line='yes', default_y=-153.21)
                Staff(2)
            with Note(default_x=398.5, default_y=-160.0):
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
            with Note(default_x=398.5, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=398.5, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
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
                    Pedal(type='start', line='yes', default_y=-153.21)
                Staff(2)
            with Note(default_x=710.77, default_y=-155.0):
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
            with Note(default_x=710.77, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=710.77, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
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
                    Pedal(type='start', line='yes', default_y=-153.21)
                Staff(2)
            with Note(default_x=1023.04, default_y=-160.0):
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
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=1023.04, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=1023.04, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
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
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='2', width=690.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(273.22)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(-145.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
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
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=187.18, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=218.72, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=250.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=281.8, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=313.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=344.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
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
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=499.48, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=531.02, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=562.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=594.1, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=625.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=657.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-151.86)
                Staff(2)
            with Note(default_x=64.11, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=64.11, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=64.11, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=125.64, default_y=-150.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=125.64, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=125.64, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-151.86)
                Staff(2)
            with Note(default_x=187.18, default_y=-145.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=187.18, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=187.18, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=281.8, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=281.8, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=281.8, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-151.86)
                Staff(2)
            with Note(default_x=376.41, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=376.41, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=376.41, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=437.95, default_y=-150.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=437.95, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=437.95, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-151.86)
                Staff(2)
            with Note(default_x=499.48, default_y=-145.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=499.48, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=499.48, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=594.1, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=594.1, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=594.1, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
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
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='3', width=646.6):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('8')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=33.74, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=72.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=111.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=149.96, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=188.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=227.45, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=266.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=304.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=343.67, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=382.41, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=421.15, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=459.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=498.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=537.38, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=576.12, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(360.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-151.86)
                Staff(2)
            with Note(default_x=33.74, default_y=-155.0):
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
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=33.74, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=33.74, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
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
                    Pedal(type='start', line='yes', default_y=-151.86)
                Staff(2)
            with Note(default_x=227.45, default_y=-160.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=227.45, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=227.45, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
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
                    Pedal(type='start', line='yes', default_y=-151.86)
                Staff(2)
            with Note(default_x=421.15, default_y=-165.0):
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
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=421.15, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=421.15, default_y=-145.0):
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
            with Backup():
                Duration(360.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(360.0)
                Voice('9')
                Staff(3)
        with Measure(number='4', width=1336.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(273.22)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef(number=1):
                    Sign('F')
                    Line(4)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=82.55, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=116.76, default_y=15.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=150.98, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=185.19, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=219.4, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=253.62, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=493.12, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=527.33, default_y=15.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=561.55, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=595.76, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=629.98, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=664.19, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=903.69, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=937.9, default_y=15.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=972.12, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1006.33, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1040.55, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1074.76, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note(default_x=82.55, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=82.55, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=82.55, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=287.83, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=287.83, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=287.83, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=493.12, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=493.12, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=493.12, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=698.4, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=698.4, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=698.4, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=903.69, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=903.69, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=903.69, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=1108.98, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=1108.98, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=1108.98, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note(default_x=287.83, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=322.05, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=356.26, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=390.48, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=424.69, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=458.9, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note(default_x=698.4, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=732.62, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=766.83, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=801.05, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=835.26, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=869.48, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note(default_x=1108.98, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=1143.19, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1177.4, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1211.62, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1245.83, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1280.05, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='5', width=698.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(273.22)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('8')
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=35.0)
                Staff(2)
            with Note(default_x=86.23, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=86.23, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=145.14, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=145.14, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=204.04, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=204.04, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=30.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=288.96, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=288.96, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-27.93, relative_y=-44.69):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=361.67, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=394.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=427.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=460.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=493.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=525.92, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=558.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=591.63, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=624.48, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=657.33, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-140.5)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-140.5)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Attributes():
                with Clef(number=3):
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-140.5)
                Staff(3)
            with Note(default_x=361.67, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=361.67, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=361.67, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-140.5)
                Staff(3)
            with Note(default_x=525.92, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=525.92, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=525.92, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='6', width=638.1):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
                with Clef(number=3):
                    Sign('F')
                    Line(4)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=35.0)
                Staff(2)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=74.66, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=74.66, default_y=0.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=135.53, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=135.53, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=30.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=222.4, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=222.4, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-27.93, relative_y=-44.69):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=297.07, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=331.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=364.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=398.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=432.84, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=466.78, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=500.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=534.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=568.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=602.55, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-140.5)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-140.5)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Attributes():
                with Clef(number=3):
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-140.5)
                Staff(3)
            with Note(default_x=297.07, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=297.07, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=297.07, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-140.5)
                Staff(3)
            with Note(default_x=466.78, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=466.78, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=466.78, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='7', width=693.61):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=64.11, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=95.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=126.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=158.09, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=190.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=222.09, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=253.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=284.74, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=316.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=347.4, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=378.73, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=410.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=441.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=472.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=504.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=535.37, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=566.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=598.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=629.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=660.68, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-144.54)
                Staff(3)
            with Note(default_x=64.11, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=64.11, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=64.11, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-144.54)
                Staff(3)
            with Note(default_x=222.09, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=222.09, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=222.09, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-144.54)
                Staff(3)
            with Note(default_x=378.73, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=378.73, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=378.73, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-144.54)
                Staff(3)
            with Note(default_x=535.37, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=535.37, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=535.37, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='8', width=643.3):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=76.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=107.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=140.45, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=171.78, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=203.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=234.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=265.76, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=297.09, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=328.42, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=359.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=391.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=422.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=453.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=485.06, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=516.39, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=547.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=579.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=610.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-144.54)
                Staff(3)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=13.8, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-144.54)
                Staff(3)
            with Note(default_x=171.78, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=171.78, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=171.78, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-144.54)
                Staff(3)
            with Note(default_x=328.42, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=328.42, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=328.42, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-144.54)
                Staff(3)
            with Note(default_x=485.06, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=485.06, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=485.06, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='9', width=688.04):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(281.97)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(66.22)
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=59.8, default_y=-221.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=91.13, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=122.46, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=153.8, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=185.13, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-90.27)
                Staff(2)
            with Note(default_x=216.46, default_y=-221.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=247.79, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=279.12, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=310.46, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=341.79, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=373.12, default_y=-221.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=404.45, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=435.78, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=467.12, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=498.45, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=529.78, default_y=-221.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=561.11, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=592.45, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=623.78, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=655.11, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-111.8)
                Staff(3)
            with Note(default_x=59.8, default_y=-241.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=59.8, default_y=-231.22):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=59.8, default_y=-221.22):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=216.46, default_y=-241.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=216.46, default_y=-231.22):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=216.46, default_y=-221.22):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=373.12, default_y=-241.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=373.12, default_y=-231.22):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=373.12, default_y=-221.22):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=529.78, default_y=-241.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=529.78, default_y=-231.22):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=529.78, default_y=-221.22):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='10', width=648.88):
            with Note(default_x=16.87, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Tenuto()
                        Accent()
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-50.59, relative_x=-27.93, relative_y=-44.69):
                        OtherDynamics('più ')
                        Pp()
                Staff(2)
                Sound(dynamics=30.0)
            with Note(default_x=17.23, default_y=-221.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.73, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=80.24, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=111.74, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=143.24, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=174.74, default_y=-221.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=206.24, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=237.75, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=269.25, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=300.75, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=332.25, default_y=-221.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=363.76, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=395.26, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=426.76, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=458.26, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=489.76, default_y=-221.22):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=521.27, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=552.77, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=584.27, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=615.77, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-111.8)
                Staff(3)
            with Note(default_x=17.23, default_y=-241.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=17.23, default_y=-231.22):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=17.23, default_y=-221.22):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=174.74, default_y=-241.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=174.74, default_y=-231.22):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=174.74, default_y=-221.22):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=332.25, default_y=-241.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=332.25, default_y=-231.22):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=332.25, default_y=-221.22):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=489.76, default_y=-241.22):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=489.76, default_y=-231.22):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=489.76, default_y=-221.22):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='11', width=697.88):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(281.97)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(default_x=96.27, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Accidental('sharp', parentheses='yes')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=59.8, default_y=-45.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Octave(4)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=96.27, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
                        Accent()
            with Backup():
                Duration(480.0)
            with Note(default_x=96.63, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=126.62, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=156.6, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=186.58, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=216.56, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=246.55, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=276.53, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=306.51, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=336.49, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=366.48, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=396.46, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=426.44, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=456.42, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=486.41, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=516.39, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=546.37, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=576.35, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=606.34, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=636.32, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=666.3, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-111.67)
                Staff(3)
            with Note(default_x=96.63, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=96.63, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=96.63, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=246.55, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=246.55, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=246.55, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=396.46, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=396.46, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=396.46, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=546.37, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=546.37, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=546.37, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='12', width=639.03):
            with Note(default_x=4.75, default_y=5.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=37.42, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
                        Accent()
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=301.14, default_y=-45.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Octave(4)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=337.61, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
                        Accent()
            with Backup():
                Duration(480.0)
            with Note(default_x=37.78, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=67.77, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=97.75, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=127.73, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=157.71, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=187.7, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=217.68, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=247.66, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=277.64, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=307.63, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=337.61, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=367.59, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=397.57, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=427.56, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=457.54, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=487.52, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=517.5, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=547.49, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=577.47, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=607.45, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-111.67)
                Staff(3)
            with Note(default_x=37.78, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=37.78, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=37.78, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=187.7, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=187.7, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=187.7, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=337.61, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=337.61, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=337.61, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=487.52, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=487.52, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=487.52, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='13', width=671.64):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(281.97)
                with StaffLayout(number=2):
                    StaffDistance(68.68)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=63.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=366.82, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
                        Accent()
            with Backup():
                Duration(480.0)
            with Note(default_x=63.6, default_y=-223.68):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=93.92, default_y=-118.68):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=124.24, default_y=-123.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=154.57, default_y=-133.68):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=184.89, default_y=-143.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=215.21, default_y=-223.68):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=245.53, default_y=-118.68):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=275.85, default_y=-123.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=306.18, default_y=-133.68):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=336.5, default_y=-143.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=366.82, default_y=-223.68):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=397.14, default_y=-118.68):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=427.46, default_y=-123.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=457.78, default_y=-133.68):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=488.11, default_y=-143.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=518.43, default_y=-223.68):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=548.75, default_y=-118.68):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=579.07, default_y=-123.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=609.39, default_y=-133.68):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=639.72, default_y=-143.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-129.35)
                Staff(3)
            with Note(default_x=63.6, default_y=-243.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=63.6, default_y=-233.68):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=63.6, default_y=-223.68):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=215.21, default_y=-243.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=215.21, default_y=-233.68):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=215.21, default_y=-223.68):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=366.82, default_y=-243.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=366.82, default_y=-233.68):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=366.82, default_y=-223.68):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=518.43, default_y=-243.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=518.43, default_y=-233.68):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=518.43, default_y=-223.68):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='14', width=665.28):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=21.39, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Tenuto()
                        Accent()
            with Backup():
                Duration(480.0)
            with Note(default_x=21.75, default_y=-223.68):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=53.77, default_y=-118.68):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=85.78, default_y=-123.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=117.79, default_y=-133.68):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=149.8, default_y=-143.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=181.81, default_y=-233.68):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=213.83, default_y=-123.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=245.84, default_y=-133.68):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=277.85, default_y=-143.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=309.86, default_y=-153.68):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=341.87, default_y=-238.68):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=373.89, default_y=-133.68):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=405.9, default_y=-143.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=437.91, default_y=-153.68):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=471.61, default_y=-158.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=503.62, default_y=-233.68):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=535.63, default_y=-123.68):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=567.64, default_y=-133.68):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=599.66, default_y=-143.68):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=631.67, default_y=-153.68):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-129.35)
                Staff(3)
            with Note(default_x=21.75, default_y=-243.68):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=21.75, default_y=-233.68):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=21.75, default_y=-223.68):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=181.81, default_y=-253.68):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=181.81, default_y=-243.68):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=181.81, default_y=-233.68):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=341.87, default_y=-258.68):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=341.87, default_y=-248.68):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=341.87, default_y=-238.68):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=503.62, default_y=-253.68):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=503.62, default_y=-243.68):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=503.62, default_y=-233.68):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
        with Measure(number='15', width=705.29):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(80.26)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=63.6, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=63.96, default_y=-235.26):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=95.86, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=127.75, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=159.65, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=191.55, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=223.44, default_y=-245.26):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=255.34, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=287.23, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=319.13, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=351.03, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=382.92, default_y=-250.26):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=414.82, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=446.72, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=478.61, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=512.31, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=544.2, default_y=-245.26):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=576.1, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=608.0, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=639.89, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=671.79, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note(default_x=63.96, default_y=-255.26):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=63.96, default_y=-245.26):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=63.96, default_y=-235.26):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=223.44, default_y=-265.26):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=223.44, default_y=-255.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=223.44, default_y=-245.26):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=382.92, default_y=-270.26):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=382.92, default_y=-260.26):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=382.92, default_y=-250.26):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=544.2, default_y=-265.26):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=544.2, default_y=-255.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=544.2, default_y=-245.26):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='16', width=304.56):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Cédez - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=43.5)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_x=27.93, relative_y=-44.69):
                        OtherDynamics('più ')
                        Pp()
                Staff(2)
                Sound(dynamics=23.33)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=156.95, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Tenuto()
                    Arpeggiate(default_x=-31.12, default_y=-9.49)
            with Note(default_x=156.95, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    Arpeggiate(default_x=-31.12, default_y=-9.49)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-128.35)
                Staff(3)
            with Note(default_x=10.94, default_y=-255.26):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=10.94, default_y=-245.26):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=10.94, default_y=-235.26):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=83.94, default_y=-265.26):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=83.94, default_y=-255.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=83.94, default_y=-245.26):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-128.35)
                Staff(3)
            with Note(default_x=156.95, default_y=-270.26):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=156.95, default_y=-260.26):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=156.95, default_y=-250.26):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=229.96, default_y=-265.26):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=229.96, default_y=-255.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=229.96, default_y=-245.26):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=25.66, relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('86')
                Offset(-360.0)
                Staff(1)
                Sound(tempo=43.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=25.66, relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('85')
                Offset(-240.0)
                Staff(1)
                Sound(tempo=42.5)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=25.66, relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('84')
                Offset(-120.0)
                Staff(1)
                Sound(tempo=42.0)
        with Measure(number='17', width=327.07):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=25.66, relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('83')
                Staff(1)
                Sound(tempo=41.5)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
                with Notations():
                    with Articulations():
                        Caesura(None)
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=158.66, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
                    Arpeggiate(default_x=-31.12, default_y=-9.49)
            with Note(default_x=158.66, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=-9.49)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-128.35)
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=39.1)
                Staff(3)
            with Note(default_x=13.8, default_y=-270.26):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-260.26):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-250.26):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=86.23, default_y=-265.26):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=86.23, default_y=-255.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=86.23, default_y=-245.26):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-128.35)
                Staff(3)
            with Note(default_x=158.66, default_y=-270.26):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=158.66, default_y=-260.26):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=158.66, default_y=-250.26):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=22.72)
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=4.1, relative_y=30.0):
                        Ppp()
                Staff(3)
                Sound(dynamics=17.78)
            with Note(default_x=231.08, default_y=-265.26):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=231.08, default_y=-255.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=231.08, default_y=-245.26):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=25.66, relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('82')
                Offset(-360.0)
                Staff(1)
                Sound(tempo=41.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=25.66, relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('81')
                Offset(-240.0)
                Staff(1)
                Sound(tempo=40.5)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('80')
                Offset(-120.0)
                Staff(1)
                Sound(tempo=40.0)
        with Measure(number='18', width=414.75):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(224.19)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(88.62)
            with Attributes():
                with Clef(number=3):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Mouvt.', default_y=68.96, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=44.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=74.89)
                Staff(1)
            with Note(default_x=77.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=77.21, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=135.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
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
            with Note(default_x=135.13, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=193.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=193.05, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=320.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=320.48, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('un peu en dehors', default_y=-40.0, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(2)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-56.8, relative_y=-40.0):
                        Pp()
                Staff(3)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-136.6)
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='up', size=8, number=2, default_y=-104.89)
                Staff(3)
            with Note(default_x=77.21, default_y=-293.62):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(1)
                Duration(60.0)
                Voice('9')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=77.21, default_y=-258.62):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('9')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-136.6)
                Staff(3)
            with Note(default_x=135.13, default_y=-288.62):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(60.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=135.13, default_y=-253.62):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(60.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=193.05, default_y=-288.62):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=193.05, default_y=-253.62):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-136.6)
                Staff(3)
            with Note(default_x=320.48, default_y=-273.62):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=320.48, default_y=-238.62):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='19', width=350.84):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=21.03, default_y=-10.0):
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
                    with Articulations():
                        Staccato()
            with Note(default_x=21.03, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=112.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=112.2, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(7)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=258.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=258.07, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
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
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-136.6)
                Staff(3)
            with Note(default_x=21.03, default_y=-288.62):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(1)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=21.03, default_y=-253.62):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-136.6)
                Staff(3)
            with Note(default_x=112.2, default_y=-273.62):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=112.2, default_y=-238.62):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-136.6)
                Staff(3)
            with Note(default_x=258.07, default_y=-283.62):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=258.07, default_y=-248.62):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='20', width=571.33):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-44.1, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-79.1)
                Staff(1)
            with Note(default_x=21.03, default_y=-15.0):
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
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=21.03, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=61.07)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-44.1, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=109.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=109.84, default_y=20.0):
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
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=30.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=198.64, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=235.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=272.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=309.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=347.08, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=384.19, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=421.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=458.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=495.51, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=532.62, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(240.0)
            with Note(default_x=198.64, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=198.64, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=198.64, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=384.19, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=384.19, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=384.19, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-136.6)
                Staff(3)
            with Note(default_x=21.03, default_y=-293.62):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(1)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='below', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=21.03, default_y=-258.62):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=2)
                Staff(3)
            with Note(default_x=109.84, default_y=-258.62):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('9')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(3)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
                    with Articulations():
                        Tenuto()
            with Note(default_x=109.84, default_y=-223.62):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('9')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='21', width=576.42):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(224.19)
                with StaffLayout(number=2):
                    StaffDistance(71.39)
                with StaffLayout(number=3):
                    StaffDistance(82.47)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-44.1, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-79.1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=71.85)
                Staff(1)
            with Note(default_x=77.21, default_y=-15.0):
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
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=77.21, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=61.07)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-44.1, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=161.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=161.72, default_y=20.0):
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
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=5.06, relative_y=30.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=35.0)
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=30.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=35.0)
                Staff(2)
            with Note(default_x=375.49, default_y=-131.39):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=408.62, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=441.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=474.87, default_y=-136.39):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=508.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=541.69, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(240.0)
            with Note(default_x=246.23, default_y=-161.39):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=246.23, default_y=-151.39):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=246.23, default_y=-141.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=310.86, default_y=-156.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=310.86, default_y=-146.39):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=310.86, default_y=-136.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=375.49, default_y=-151.39):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=375.49, default_y=-141.39):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=375.49, default_y=-131.39):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=474.87, default_y=-156.39):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=474.87, default_y=-146.39):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=474.87, default_y=-136.39):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='up', size=8, number=1, default_y=-91.8)
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-134.86)
                Staff(3)
            with Note(default_x=77.21, default_y=-293.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(1)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='below', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=77.21, default_y=-258.87):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(3)
            with Note(default_x=161.72, default_y=-258.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('9')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(3)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
                    with Articulations():
                        Tenuto()
            with Note(default_x=161.72, default_y=-223.87):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('9')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='22', width=385.03):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=78.16)
                Staff(1)
            with Note(default_x=21.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=21.03, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=83.51, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
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
            with Note(default_x=83.51, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=146.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=146.0, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=283.46, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=283.46, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('un peu en dehors', default_y=-40.0, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(2)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-56.69, relative_y=-40.0):
                        Pp()
                Staff(3)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-134.86)
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='up', size=8, number=2, default_y=-103.16)
                Staff(3)
            with Note(default_x=21.03, default_y=-293.87):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(1)
                Duration(60.0)
                Voice('9')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=21.03, default_y=-258.87):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('9')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-134.86)
                Staff(3)
            with Note(default_x=83.51, default_y=-288.87):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(60.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=83.51, default_y=-253.87):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(60.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=146.0, default_y=-288.87):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=146.0, default_y=-253.87):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-134.86)
                Staff(3)
            with Note(default_x=283.46, default_y=-273.87):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=283.46, default_y=-238.87):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='23', width=375.47):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=107.97, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=107.97, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=258.64, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=258.64, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
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
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-134.86)
                Staff(3)
            with Note(default_x=13.8, default_y=-283.87):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-248.87):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-134.86)
                Staff(3)
            with Note(default_x=107.97, default_y=-268.87):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=107.97, default_y=-233.87):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-134.86)
                Staff(3)
            with Note(default_x=258.64, default_y=-278.87):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=258.64, default_y=-243.87):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='24', width=1336.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(224.19)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(90.43)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-44.1, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-79.1)
                Staff(1)
            with Note(default_x=98.27, default_y=-15.0):
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
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=98.27, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=61.07)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-44.1, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=215.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=215.67, default_y=20.0):
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
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(720.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=30.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=333.08, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=382.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=431.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=480.26, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=529.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=578.38, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=627.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=676.49, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=725.55, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=774.61, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=823.67, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=872.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=921.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=970.85, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1019.91, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=1068.97, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=1118.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1167.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1216.14, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1265.2, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(720.0)
            with Forward():
                Duration(240.0)
            with Note(default_x=333.08, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=333.08, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=333.08, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=578.38, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=578.38, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=578.38, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=823.67, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=823.67, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=823.67, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=1068.97, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=1068.97, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=1068.97, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(720.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-114.41)
                Staff(3)
            with Note(default_x=98.27, default_y=-295.43):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(1)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='below', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=98.27, default_y=-260.43):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=2)
                Staff(3)
            with Note(default_x=215.67, default_y=-260.43):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(360.0)
                Voice('9')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(3)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
                    with Articulations():
                        Tenuto()
            with Note(default_x=215.67, default_y=-225.43):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(360.0)
                Voice('9')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-114.41)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-114.41)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='25', width=699.8):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(-145.0)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('8')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
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
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=206.8, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=237.71, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=268.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=299.51, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=330.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=361.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note():
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-42.86, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-77.86)
                Staff(1)
            with Note(default_x=512.79, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=543.69, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=574.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=605.49, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=636.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=667.3, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-151.75)
                Staff(2)
            with Note(default_x=86.23, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=86.23, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=86.23, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=146.52, default_y=-150.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=146.52, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=146.52, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-151.75)
                Staff(2)
            with Note(default_x=206.8, default_y=-145.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=206.8, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=206.8, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=299.51, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=299.51, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=299.51, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-151.75)
                Staff(2)
            with Note(default_x=392.21, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=392.21, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=392.21, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=452.5, default_y=-150.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=452.5, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=452.5, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-151.75)
                Staff(2)
            with Note(default_x=512.79, default_y=-145.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=512.79, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=512.79, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=605.49, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=605.49, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=605.49, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
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
            with Backup():
                Duration(480.0)
            with Note():
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='26', width=637.12):
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('8')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-26.79, relative_y=-42.86):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=33.74, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=71.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=109.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=148.07, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=186.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=224.29, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=262.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=300.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=338.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=376.72, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=414.83, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=452.94, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=491.05, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=529.16, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=567.27, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(360.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-151.75)
                Staff(2)
            with Note(default_x=33.74, default_y=-155.0):
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
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=33.74, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=33.74, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
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
                    Pedal(type='start', line='yes', default_y=-151.75)
                Staff(2)
            with Note(default_x=224.29, default_y=-160.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=224.29, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=224.29, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
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
                    Pedal(type='start', line='yes', default_y=-151.75)
                Staff(2)
            with Note(default_x=414.83, default_y=-165.0):
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
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=414.83, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=414.83, default_y=-145.0):
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
            with Backup():
                Duration(360.0)
            with Note():
                Rest(measure='yes')
                Duration(360.0)
                Voice('9')
                Staff(3)
        with Measure(number='27', width=684.62):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(340.14)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('4')
                    BeatType('8')
                with Clef(number=1):
                    Sign('F')
                    Line(4)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=82.43, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=106.35, default_y=15.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=137.02, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=165.88, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=194.75, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=223.62, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=391.05, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=414.97, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=438.89, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=462.81, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=486.72, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=515.59, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=539.51, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=563.43, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=587.35, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=611.27, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=635.18, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=659.1, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note(default_x=82.43, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=82.43, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=82.43, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=247.53, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=247.53, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=247.53, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=391.05, default_y=-130.0):
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
            with Note(default_x=391.05, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=391.05, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=539.51, default_y=-125.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=539.51, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=539.51, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note(default_x=247.53, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=271.45, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=295.37, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=319.29, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=343.21, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=367.13, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='28', width=652.29):
            with Note(default_x=13.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.24, default_y=15.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=69.91, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=98.77, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=127.64, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=156.5, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=334.55, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=359.99, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=385.42, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=410.86, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=436.29, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=465.16, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=490.59, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=516.03, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=542.69, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=568.13, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=594.79, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=625.26, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=181.94, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=181.94, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=181.94, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=334.55, default_y=-130.0):
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
            with Note(default_x=334.55, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=334.55, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=490.59, default_y=-110.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=490.59, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=490.59, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note(default_x=181.94, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=207.37, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=232.81, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=258.24, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=283.68, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=309.12, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(20.0)
                Voice('9')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='29', width=709.42):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(340.14)
                with StaffLayout(number=2):
                    StaffDistance(124.96)
                with StaffLayout(number=3):
                    StaffDistance(-204.96)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=8.34, default_y=-58.19, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-93.19)
                Staff(1)
            with Note():
                Rest()
                Duration(15.0)
                Voice('1')
                Type('64th')
                Staff(1)
            with Note(default_x=98.7, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=130.03, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=162.83, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=186.1, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Note(default_x=225.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=265.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=313.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=328.67, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=344.34, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=375.67, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=408.48, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=431.74, default_y=40.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=107.21)
                Staff(1)
            with Note(default_x=451.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=483.28, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=516.08, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(7)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-58.19, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=539.35, default_y=40.0):
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.53, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note():
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-117.63)
                Staff(2)
            with Note(default_x=73.41, default_y=-209.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Backup():
                Duration(140.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Forward():
                Duration(140.0)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=582.67, default_y=-214.96):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(4)
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
            with Note(default_x=582.67, default_y=-204.96):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=582.67, default_y=-194.96):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=611.23, default_y=-45.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=611.23, default_y=-30.0):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=611.23, default_y=-20.0):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=651.93, default_y=-204.96):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=651.93, default_y=-194.96):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural', parentheses='yes')
                Stem('up')
                Staff(2)
            with Note(default_x=651.93, default_y=-179.96):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(default_x=73.41, default_y=-209.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=114.36, default_y=-189.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=146.43, default_y=-174.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=186.1, default_y=-164.96):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=241.23, default_y=-154.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=297.34, default_y=-199.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=328.67, default_y=-189.96):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=360.0, default_y=-179.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=392.07, default_y=-164.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=431.74, default_y=-154.96):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=466.87, default_y=-144.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=500.05, default_y=-129.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=539.35, default_y=-119.96):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(300.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='30', width=627.49):
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=8.34, default_y=-58.19, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-93.19)
                Staff(1)
            with Note():
                Rest()
                Duration(15.0)
                Voice('1')
                Type('64th')
                Staff(1)
            with Note(default_x=42.52, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                Beam('begin', number=4)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=73.85, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=106.65, default_y=25.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=129.92, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Note(default_x=169.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=209.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=256.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=272.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=288.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=319.49, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=352.29, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=375.56, default_y=40.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=107.21)
                Staff(1)
            with Note(default_x=395.03, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=427.09, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                Beam('continue', number=4)
            with Note(default_x=459.9, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(7)
                Duration(15.0)
                Voice('1')
                Type('64th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                Beam('end', number=4)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-58.19, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=483.17, default_y=40.0):
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(60.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.53, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note():
                Rest()
                Duration(60.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-117.63)
                Staff(2)
            with Note(default_x=17.23, default_y=-209.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Backup():
                Duration(140.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Forward():
                Duration(140.0)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=531.12, default_y=-209.96):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Octave(4)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=531.12, default_y=-199.96):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=531.12, default_y=-189.96):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=561.22, default_y=-40.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=561.22, default_y=-25.0):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=561.22, default_y=-15.0):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('5')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=593.12, default_y=-199.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=593.12, default_y=-189.96):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Accidental('natural', parentheses='yes')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=593.12, default_y=-174.96):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(480.0)
            with Note(default_x=17.23, default_y=-209.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=58.18, default_y=-189.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=90.25, default_y=-174.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=129.92, default_y=-164.96):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=185.04, default_y=-154.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=241.16, default_y=-199.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=272.49, default_y=-189.96):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=303.82, default_y=-179.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=335.89, default_y=-164.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=375.56, default_y=-154.96):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=410.69, default_y=-144.96):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=443.87, default_y=-129.96):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('6')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(12)
                    NormalNotes(8)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=483.17, default_y=-119.96):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(6)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(300.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='31', width=351.86):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(340.14)
                with StaffLayout(number=2):
                    StaffDistance(66.29)
                with StaffLayout(number=3):
                    StaffDistance(-146.29)
            with Note():
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=81.65, default_y=-141.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Accidental('sharp', parentheses='yes')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=81.65, default_y=-131.29):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=81.65, default_y=-116.29):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=35.0)
                Staff(2)
            with Note(default_x=215.96, default_y=-141.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=215.96, default_y=-131.29):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=215.96, default_y=-116.29):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='32', width=985.05):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Un peu retenu', relative_y=55.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=40.0)
            with Note(default_x=17.23, default_y=-116.29):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=74.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=104.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=131.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=170.73, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=204.42, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=47.42)
                Staff(1)
            with Note(default_x=231.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=261.35, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=295.05, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=322.08, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=349.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=376.14, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=403.18, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=430.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=457.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=484.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=511.3, default_y=-116.29):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=538.34, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=565.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=592.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=619.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=659.07, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=686.1, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=47.3)
                Staff(1)
            with Note(default_x=713.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=740.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=767.2, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=794.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=821.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=848.29, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=875.32, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=902.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=929.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=956.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=13.75, relative_x=-15.0, relative_y=30.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.42)
                Staff(2)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('5')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(default_x=17.23, default_y=-141.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=17.23, default_y=-131.29):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.42)
                Staff(2)
            with Note(default_x=511.3, default_y=-141.29):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=511.3, default_y=-131.29):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='33', width=1336.92):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(-145.0)
            with Note(default_x=72.35, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=107.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=143.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=178.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=214.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=261.89, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=297.37, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=47.42)
                Staff(1)
            with Note(default_x=332.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=368.34, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=419.96, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=455.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=490.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=526.41, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=561.89, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=597.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=632.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=668.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=703.83, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=739.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=774.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=810.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=845.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=893.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=928.86, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=37.92)
                Staff(1)
            with Note(default_x=964.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=999.82, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1051.44, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1086.92, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1122.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=1157.89, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1193.38, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1228.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1264.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1299.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-93.97)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-124.46)
                Staff(2)
            with Note(default_x=72.35, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-58.97, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-124.46)
                Staff(2)
            with Note(default_x=394.15, default_y=-110.0):
                with Pitch():
                    Step('E')
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-93.97)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-124.46)
                Staff(2)
            with Note(default_x=703.83, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-58.97, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-124.46)
                Staff(2)
            with Note(default_x=1025.63, default_y=-125.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(default_x=72.35, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=72.35, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('6')
                Type('16th')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=703.83, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=703.83, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('6')
                Type('16th')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='34', width=1336.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(259.87)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(-145.0)
            with Note(default_x=72.35, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=108.29, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=144.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=180.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=216.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=264.34, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=300.28, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=47.42)
                Staff(1)
            with Note(default_x=336.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=372.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=408.11, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=444.06, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=480.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=515.95, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=551.89, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=587.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=623.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=659.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=695.66, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=731.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=767.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=803.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=839.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=887.65, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=923.6, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=37.92)
                Staff(1)
            with Note(default_x=959.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=995.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1047.77, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1083.71, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1119.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=1155.6, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1191.54, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1227.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1263.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1299.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.42)
                Staff(2)
            with Note(default_x=72.35, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=232.46, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.42)
                Staff(2)
            with Note(default_x=695.66, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-104.42)
                Staff(2)
            with Note(default_x=1021.63, default_y=-120.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(default_x=84.22, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=84.22, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=707.53, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=707.53, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('6')
                Type('16th')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='35', width=1336.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(259.87)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(-145.0)
            with Note(default_x=72.35, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=107.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=143.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=178.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=214.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=261.89, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=297.37, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=47.42)
                Staff(1)
            with Note(default_x=332.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=368.34, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=419.96, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=455.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=490.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=526.41, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=561.89, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=597.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=632.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=668.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=703.83, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=739.32, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=774.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=810.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=845.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=893.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=928.86, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=42.42)
                Staff(1)
            with Note(default_x=964.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=999.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1051.44, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1086.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1122.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=1157.89, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1193.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1228.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1264.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1299.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-109.42)
                Staff(2)
            with Note(default_x=72.35, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-109.42)
                Staff(2)
            with Note(default_x=703.83, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(print_object='no'):
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
                Duration(480.0)
            with Note(default_x=72.35, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=72.35, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Note(default_x=703.83, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=703.83, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='36', width=1336.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(259.87)
                with StaffLayout(number=2):
                    StaffDistance(67.19)
                with StaffLayout(number=3):
                    StaffDistance(-147.19)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-25.0, relative_y=-40.0):
                        OtherDynamics('più ')
                        Pp()
                Staff(1)
                Sound(dynamics=27.78)
            with Note(default_x=64.11, default_y=-137.19):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=100.17, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=136.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=172.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=208.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=256.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=292.79, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=328.85, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=364.92, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=417.37, default_y=45.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=453.43, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=489.5, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=525.56, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=561.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=597.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=633.74, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=669.81, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=705.87, default_y=-137.19):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=741.93, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=777.99, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=814.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=850.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=886.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=922.24, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=958.3, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=994.37, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1046.82, default_y=45.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1082.88, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1118.94, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1155.01, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1191.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1227.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1263.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1299.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-124.42)
                Staff(2)
            with Note(default_x=64.11, default_y=-137.19):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-124.42)
                Staff(2)
            with Note(default_x=391.14, default_y=-127.19):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-124.42)
                Staff(2)
            with Note(default_x=705.87, default_y=-137.19):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-124.42)
                Staff(2)
            with Note(default_x=1020.59, default_y=-147.19):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(default_x=64.11, default_y=-162.19):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=64.11, default_y=-152.19):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('6')
                Type('16th')
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
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='37', width=1336.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(259.87)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(-145.0)
            with Note(default_x=61.37, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=97.98, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=134.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=171.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=207.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=256.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=293.54, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=330.15, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=366.76, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=403.38, default_y=45.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=439.99, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=476.6, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=513.21, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=549.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=586.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=623.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=659.66, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=696.27, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=732.88, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=769.5, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=806.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=842.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=879.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=915.94, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=952.56, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=989.17, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1042.42, default_y=45.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1079.03, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1115.65, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1152.26, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1188.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1225.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=1262.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Tie(type='start')
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='start')
            with Note(default_x=1298.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Tie(type='start')
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='stop')
            with Note(default_x=1298.71, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(14.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(17)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-101.79)
                Staff(2)
            with Note(default_x=61.37, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=224.46, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(180.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-101.79)
                Staff(2)
            with Note(default_x=696.27, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-101.79)
                Staff(2)
            with Note(default_x=1015.79, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(default_x=73.24, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=73.24, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='38', width=300.51):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(81.8)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Mouvt.', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=44.0)
            with Note(default_x=122.77, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=122.77, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=122.77, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(480.0)
            with Note(default_x=110.18, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.18, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.18, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Pp()
                Staff(3)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-126.24)
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='up', size=8, number=1, default_y=-94.53)
                Staff(3)
            with Note(default_x=110.54, default_y=-286.8):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(1)
                Duration(60.0)
                Voice('9')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=110.54, default_y=-251.8):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('9')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-126.24)
                Staff(3)
            with Note(default_x=143.02, default_y=-281.8):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(60.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=143.02, default_y=-246.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(60.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=175.5, default_y=-281.8):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=175.5, default_y=-246.8):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-126.24)
                Staff(3)
            with Note(default_x=246.95, default_y=-266.8):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=246.95, default_y=-231.8):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='39', width=191.33):
            with Note(default_x=36.56, default_y=-60.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=36.56, default_y=-45.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=36.56, default_y=-25.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=20.67, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=20.67, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=20.67, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-80.19)
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-126.24)
                Staff(3)
            with Note(default_x=21.03, default_y=-281.8):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(1)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=21.03, default_y=-246.8):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=32.66)
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-45.19, relative_y=-40.0):
                        P()
                Staff(3)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-126.24)
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.19, relative_x=73.85)
                Staff(3)
            with Note(default_x=65.27, default_y=-266.8):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=65.27, default_y=-231.8):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-126.24)
                Staff(3)
            with Note(default_x=136.05, default_y=-276.8):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=136.05, default_y=-241.8):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='40', width=533.93):
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=4.61, default_y=-40.0, relative_x=-25.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=75.64, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=97.97, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=124.11, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=139.78, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=155.44, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=174.76, default_y=30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=200.61, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=228.36, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=250.7, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Note(default_x=272.75, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=299.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('natural', parentheses='yes')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=314.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=330.59, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=346.25, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=368.59, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=384.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=399.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=415.59, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=431.25, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=450.57, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=466.23, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=481.9, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=497.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=513.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(24)
                    NormalNotes(8)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-51.29, relative_y=-40.0):
                        Pp()
                Staff(3)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-126.24)
                Staff(3)
            with Note(default_x=20.67, default_y=-286.8):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(1)
                Duration(480.0)
                Voice('9')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=20.67, default_y=-251.8):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(480.0)
                Voice('9')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='41', width=311.15):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=32.7, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Tenuto()
            with Note(default_x=32.7, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=32.7, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(30.0)
                Voice('5')
                Type('32nd')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-48.39, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-83.39)
                Staff(2)
            with Note(default_x=55.93, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Words('un peu marqué', default_y=-76.36, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(2)
            with Note(default_x=79.2, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=102.06, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=135.76, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-48.39, relative_y=-40.0):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Note(default_x=172.35, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Tie(type='start')
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=208.93, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=259.24, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(360.0)
                Voice('9')
                Type('quarter')
                Dot()
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-126.24)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
        with Measure(number='42', width=226.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(261.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(87.01)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Cédez - - - - - - - - - - - - - ', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=42.0)
            with Note(default_x=64.11, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    with Articulations():
                        Caesura(None)
            with Note(default_x=64.11, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.11, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=64.11, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(480.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Pp()
                Staff(3)
                Sound(dynamics=36.67)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=35.0)
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='up', size=8, number=1, default_y=-87.86)
                Staff(3)
            with Note(default_x=134.62, default_y=-282.01):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(240.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(3)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=25.66, relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('80')
                Offset(-240.0)
                Staff(1)
                Sound(tempo=40.0)
        with Measure(number='43', width=396.19):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words("Mouvt., en retenant et en s'effaçant", default_y=28.18, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=44.0)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=100.95, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=129.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=158.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=187.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=216.94, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Note(default_x=245.94, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=274.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=303.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=332.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=365.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=-30.0, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-141.87)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-141.87)
                Staff(2)
            with Note(default_x=100.95, default_y=-155.0):
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
                    Slur(type='start', placement='below', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=100.95, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=100.95, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=245.94, default_y=-160.0):
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
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=245.94, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=245.94, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Pp()
                Staff(3)
                Sound(dynamics=27.78)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-112.01)
                Staff(3)
            with Note(default_x=13.8, default_y=-292.01):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(480.0)
                Voice('9')
                Type('half')
                Stem('up')
                Staff(3)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='44', width=318.16):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('87')
                Staff(1)
                Sound(tempo=43.5)
            with Note(print_object='no'):
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
            with Note(default_x=169.56, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=191.6, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=220.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=242.5, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=264.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=293.4, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=83.59, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=83.59, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=83.59, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=126.58, default_y=-150.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=126.58, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=126.58, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=169.56, default_y=-145.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=169.56, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=169.56, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=242.5, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=242.5, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=242.5, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-112.01)
                Staff(3)
            with Note(default_x=13.8, default_y=-292.01):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(480.0)
                Voice('9')
                Type('half')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='45', width=396.19):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('86')
                Staff(1)
                Sound(tempo=43.0)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=100.95, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=129.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=158.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=187.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=216.94, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=245.94, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=274.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=303.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=332.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=365.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=100.95, default_y=-155.0):
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
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=100.95, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=100.95, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=245.94, default_y=-160.0):
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
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=245.94, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=245.94, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-112.01)
                Staff(3)
            with Note(default_x=13.8, default_y=-292.01):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(480.0)
                Voice('9')
                Type('half')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='46', width=474.09):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(261.43)
                with StaffLayout(number=2):
                    StaffDistance(66.1)
                with StaffLayout(number=3):
                    StaffDistance(87.56)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('85')
                Staff(1)
                Sound(tempo=42.5)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=155.82, default_y=-136.1):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=187.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=218.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=250.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=282.05, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=313.6, default_y=-141.1):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=345.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=376.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=408.27, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=440.93, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(480.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=155.82, default_y=-156.1):
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
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=155.82, default_y=-146.1):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=155.82, default_y=-136.1):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=313.6, default_y=-161.1):
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
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=313.6, default_y=-151.1):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=313.6, default_y=-141.1):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.21)
                Staff(3)
            with Note(default_x=61.01, default_y=-293.66):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(480.0)
                Voice('9')
                Type('half')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='47', width=422.69):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('84')
                Staff(1)
                Sound(tempo=42.0)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=218.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=218.55, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=218.55, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=35.5)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=353.58, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=353.58, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-50.49, relative_y=-40.0):
                        Ppp()
                Staff(2)
                Sound(dynamics=17.78)
            with Note(default_x=26.03, default_y=-156.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=72.06, default_y=-151.1):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
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
            with Note(default_x=98.53, default_y=-136.1):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Tie(type='start')
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
                with Notations():
                    Tied(type='start')
            with Note(default_x=124.99, default_y=-30.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=124.99, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=153.82, default_y=-30.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=153.82, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=186.48, default_y=-30.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
                    Tuplet(type='stop')
            with Note(default_x=186.48, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(20.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(6)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
            with Note(default_x=218.55, default_y=-151.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=218.55, default_y=-136.1):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=353.58, default_y=-136.1):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(default_x=40.67, default_y=-156.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=2)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.21)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.21)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.21)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='48', width=440.14):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=23.44, relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('83')
                Staff(1)
                Sound(tempo=41.5)
            with Note(default_x=20.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=20.0, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(240.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=81.37, default_y=-136.1):
                Cue()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=107.27, default_y=-131.1):
                Cue()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=133.18, default_y=-101.1):
                Cue()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=159.08, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='start')
            with Note(default_x=184.98, default_y=10.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
                    Tuplet(type='stop')
            with Note(default_x=184.98, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(12.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=215.67, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(360.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=215.67, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(360.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-112.66)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-112.66)
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=81.37, default_y=-136.1, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=107.27, default_y=-136.1, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=107.27, default_y=-131.1, print_object='no'):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=133.18, default_y=-136.1, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=133.18, default_y=-131.1, print_object='no'):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=133.18, default_y=-101.1, print_object='no'):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=159.08, default_y=-136.1, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=159.08, default_y=-131.1, print_object='no'):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=159.08, default_y=-101.1, print_object='no'):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=184.98, default_y=-136.1, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
                    Tuplet(type='stop')
            with Note(default_x=184.98, default_y=-131.1, print_object='no'):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=184.98, default_y=-101.1, print_object='no'):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=215.67, default_y=-136.1):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(360.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=227.54, default_y=-131.1):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(360.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=215.67, default_y=-101.1):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(360.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=20.0, default_y=-156.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=289.96, default_y=-156.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=289.96, default_y=-146.1):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=289.96, default_y=-136.1):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=364.25, default_y=-161.1):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Tie(type='start')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=364.25, default_y=-151.1):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=364.25, default_y=-141.1):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(480.0)
            with Note(default_x=20.0, default_y=-146.1):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Backup():
                Duration(120.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.21)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.21)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.21)
                Staff(3)
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='49', width=366.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.65)
                        RightMargin(0.0)
                    SystemDistance(261.43)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(-145.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('82')
                Staff(1)
                Sound(tempo=41.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note():
                Rest(measure='yes')
                Duration(480.0)
                Voice('2')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(default_x=64.11, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.11, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.11, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=137.53, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.53, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=137.53, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=183.42, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=183.42, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=183.42, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=229.31, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=229.31, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=229.31, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('6')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=275.2, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=275.2, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=275.2, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(180.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='50', width=445.86):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('81')
                Staff(1)
                Sound(tempo=40.5)
            with Note():
                Rest()
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
            with Note(print_object='no'):
                Rest()
                Duration(120.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Forward():
                Duration(240.0)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Presque plus rien')
                with DirectionType():
                    Dashes(type='start', number=1)
                Staff(1)
            with Note(default_x=231.31, default_y=-135.0):
                Cue()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=257.37, default_y=-130.0):
                Cue()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('32nd')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=283.43, default_y=-100.0):
                Cue()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=309.5, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='start')
            with Note(default_x=335.56, default_y=10.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
                    Tuplet(type='stop')
            with Note(default_x=335.56, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(12.0)
                Voice('2')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=366.25, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=366.25, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(480.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-133.39)
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(60.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=231.31, default_y=-135.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=257.37, default_y=-135.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=257.37, default_y=-130.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=283.43, default_y=-135.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=283.43, default_y=-130.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=283.43, default_y=-100.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=309.5, default_y=-135.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=309.5, default_y=-130.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=309.5, default_y=-100.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=335.56, default_y=-135.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
                    Tuplet(type='stop')
            with Note(default_x=335.56, default_y=-130.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=335.56, default_y=-100.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('32nd', size='cue')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=366.25, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=378.12, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=366.25, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(120.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-133.39)
                Staff(2)
            with Note(default_x=88.95, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=88.95, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=88.95, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(120.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=166.96, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=166.96, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=166.96, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='51', width=257.95):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=70.01, relative_y=20.0):
                        BeatUnit('eighth')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=40.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=13.8, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(480.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-133.39)
                Staff(2)
            with Note(default_x=13.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=26.39, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=13.8, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=2)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-133.39)
                Staff(2)
            with Note(default_x=135.25, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=135.25, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=135.25, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
        with Measure(number='52', width=266.79):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('1')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(480.0)
            with Note(default_x=13.8, default_y=10.0, print_object='no'):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=45.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(480.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(480.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-65.58, relative_y=-40.0):
                        Pppp()
                Staff(2)
                Sound(dynamics=11.11)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-133.39)
                Staff(2)
            with Note(default_x=13.8, default_y=-135.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-130.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-100.0, print_object='no'):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(480.0)
            with Note(default_x=26.39, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=26.39, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=26.39, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-133.39)
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(240.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(480.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(480.0)
                Voice('9')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-heavy')