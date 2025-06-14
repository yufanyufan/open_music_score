with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Claude Debussy Berceuse Héroïque')
    with Identification():
        Creator('Claude Debussy', type='composer')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(6.256)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1898.54)
            PageWidth(1343.09)
            with PageMargins(type='even'):
                LeftMargin(63.9387)
                RightMargin(63.9387)
                TopMargin(63.9387)
                BottomMargin(127.877)
            with PageMargins(type='odd'):
                LeftMargin(63.9387)
                RightMargin(63.9387)
                TopMargin(63.9387)
                BottomMargin(127.877)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Berceuse Héroïque', default_x=671.547, default_y=1834.6, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Claude Debussy\n', default_x=1279.16, default_y=1734.6, justify='right', valign='bottom', font_size='12')
        CreditWords('1914\n')
        CreditWords(None)
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('pour rendre hommage à S.M. le Roi ALBERT 1er de Belgique\n', default_x=671.547, default_y=1780.92, justify='center', valign='top')
        CreditWords('et à ses Soldats\n')
        CreditWords(None)
    with Credit(page=1):
        CreditWords('L. 132', default_x=63.9387, default_y=1756.17, justify='left', valign='top', font_size='12')
    with Credit(page=1):
        CreditWords('Piano 4 mains', default_x=63.9387, default_y=1834.6, justify='left', valign='top')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('brace')
        with ScorePart(id='P1'):
            PartName('\n\n\n\n\n\n\n\n\n\n\n\n\nPiano')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(93.7008)
                Pan(14.0)
        with PartGroup(type='start', number='2'):
            GroupSymbol('brace')
        with ScorePart(id='P2'):
            PartName('Grand Piano', print_object='no')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(92.9134)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=385.85):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(84.98)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(-6)
                with Time():
                    Beats('2')
                    BeatType('2')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Modéré (sans lenteur) ', default_x=-54.22, relative_y=20.0, font_weight='bold', font_size='12')
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-54.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('72')
                Staff(1)
                Sound(tempo=72.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Words('grave et soutenu', default_y=-40.0, relative_x=37.15, relative_y=-48.06, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=169.58, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=223.25, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=276.91, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=330.58, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='2', width=230.07):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=67.47, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=121.13, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=174.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='3', width=249.92):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=10.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=66.08, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.12, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=136.17, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=192.24, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
        with Measure(number='4', width=264.4):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=10.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=68.3, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=104.75, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.19, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=199.49, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
        with Measure(number='5', width=358.71):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-88.18)
                Staff(2)
            with Note(default_x=130.38, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=243.56, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=142.97, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=187.33, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=256.15, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=300.52, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='6', width=202.62):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.44, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=107.05, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=60.24, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=154.22, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
        with Measure(number='7', width=238.33):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-83.41)
                Staff(2)
            with Note(default_x=10.0, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=123.19, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=22.59, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=66.95, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=135.77, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=180.14, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='8', width=211.74):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.44, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=111.61, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=62.52, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=161.06, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
        with Measure(number='9', width=182.96):
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', default_y=9.09, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Retenu')
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=15.75)
                Staff(1)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='10', width=292.68):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(68.21)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='11', width=199.36):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=10.17):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=151.77, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=151.77, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=27.33, relative_y=-45.11):
                        OtherDynamics('sempre ')
                        Pp()
                Staff(2)
                Sound(dynamics=44.44)
            with Note(default_x=13.8, default_y=-108.21):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-98.21):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=59.79, default_y=-113.21):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=59.79, default_y=-103.21):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=105.78, default_y=-128.21):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=105.78, default_y=-118.21):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=105.78, default_y=-103.21):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=151.77, default_y=-103.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='12', width=222.67):
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=62.57, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=93.05, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-108.21):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-98.21):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=62.57, default_y=-113.21):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=62.57, default_y=-103.21):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=93.05, default_y=-118.21):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=93.05, default_y=-108.21):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=123.17, default_y=-113.21):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=123.17, default_y=-103.21):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('6')
                Type('half')
                Staff(2)
            with Note(default_x=123.53, default_y=-128.21):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=172.3, default_y=-123.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=239.11):
            with Note(default_x=10.56, default_y=-103.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=79.99, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=132.5, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=144.36, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=132.5, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=185.01, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=196.87, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=27.48, default_y=-118.21):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=27.48, default_y=-108.21):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=79.99, default_y=-108.21):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=91.85, default_y=-103.21):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=185.01, default_y=-103.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='14', width=240.54):
            with Note(default_x=17.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=75.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=128.01, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=128.01, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=29.67, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=84.95, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=128.01, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=17.8, default_y=-113.21):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=73.09, default_y=-108.21):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='15', width=313.88):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(71.85)
            with Note(default_x=143.34, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=143.34, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=185.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=227.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=227.81, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=227.81, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=239.68, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=270.05, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=270.05, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=270.05, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=142.98, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=270.05, default_y=-106.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='16', width=207.23):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-96.03)
                Staff(1)
            with Note(default_x=27.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=72.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=116.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=161.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=14.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=27.31, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=115.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=128.52, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=128.52, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='17', width=235.02):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-45.43, relative_x=36.27, relative_y=-55.6):
                        P()
                        OtherDynamics(' expressif')
                Staff(1)
                Sound(dynamics=60.0)
            with Note(default_x=17.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=17.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=17.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=17.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=94.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=94.47, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=94.47, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=94.47, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=123.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=123.97, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=123.97, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=123.97, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=171.15, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=171.15, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=171.15, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=200.64, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=200.64, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=200.64, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Forward():
                Duration(72.0)
            with Note(default_x=171.15, default_y=-106.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=200.64, default_y=-111.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='18', width=203.22):
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=60.76, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=60.76, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=60.76, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=107.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=107.71, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=107.71, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=107.71, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=154.67, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=154.67, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=154.67, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Forward():
                Duration(24.0)
            with Note(default_x=60.76, default_y=-106.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(24.0)
            with Note(default_x=154.67, default_y=-111.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='19', width=235.02):
            with Note(default_x=17.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=17.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=17.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=17.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=94.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=94.47, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=94.47, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=94.47, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=123.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=123.97, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=123.97, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=123.97, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=171.15, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=171.15, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=171.15, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=200.64, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=200.64, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=200.64, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Forward():
                Duration(72.0)
            with Note(default_x=171.15, default_y=-106.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=200.64, default_y=-111.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='20', width=331.66):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(73.31)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-89.26)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-89.26)
                Staff(1)
            with Note(default_x=145.38, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=145.38, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=145.38, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=145.38, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=191.55, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=191.55, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=237.72, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=237.72, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=237.72, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=283.89, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=191.55, default_y=-123.31):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=191.55, default_y=-113.31):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=237.72, default_y=-113.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=283.89, default_y=-118.31):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=295.76, default_y=-113.31):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest()
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Staff(2)
            with Note(default_x=289.53, default_y=-133.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=330.09):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=1.26, relative_y=16.14):
                        P()
                Staff(1)
                Sound(dynamics=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('un peu en dehors', default_y=73.19, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(1)
            with Note(default_x=60.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Note(default_x=78.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=96.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=114.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=149.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('forward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=164.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=196.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=237.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=269.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Note(default_x=287.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=305.32, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(96.0)
            with Note(default_x=24.83, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('whole')
                Accidental('natural')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=29.41):
                        Pp()
                Staff(2)
                Sound(dynamics=44.44)
            with Note(default_x=24.83, default_y=-133.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=6.32, default_y=-118.31):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=24.83, default_y=-113.31):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='22', width=203.04):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=32.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=58.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=75.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=91.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=31.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=128.03, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=31.74, default_y=-133.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=19.15, default_y=-118.31):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=31.74, default_y=-113.31):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=128.03, default_y=-123.31):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=128.03, default_y=-113.31):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=128.03, default_y=-103.31):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=329.58):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('écho', default_y=66.43, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(1)
            with Note(default_x=59.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Note(default_x=77.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=95.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=113.86, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=148.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('forward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=164.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=196.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=236.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=268.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Note(default_x=286.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=304.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(96.0)
            with Note(default_x=24.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(96.0)
                Tie(type='start')
                Voice('2')
                Type('whole')
                Accidental('natural')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Pp()
                Staff(2)
                Sound(dynamics=36.67)
            with Note(default_x=24.32, default_y=-133.31):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=24.32, default_y=-123.31):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(96.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=24.32, default_y=-113.31):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='24', width=375.98):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(74.83)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-74.27, relative_x=5.86)
                Staff(1)
            with Note(default_x=139.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=176.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=199.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=222.42, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=5.86)
                Staff(1)
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=139.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=272.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=139.18, default_y=-134.83):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=139.18, default_y=-124.83):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=139.18, default_y=-114.83):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=272.71, default_y=-124.83):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=272.71, default_y=-114.83):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=272.71, default_y=-104.83):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='25', width=257.27):
            with Direction(placement='above'):
                with DirectionType():
                    Words('En animant et en augmentant peu à peu', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', default_y=22.14, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=85.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=10.0, default_y=-144.83):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=10.0, default_y=-109.83):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=33.32, default_y=-114.83):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=88.91, default_y=-124.83):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=144.5, default_y=-119.83):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=200.08, default_y=-134.83):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=284.8):
            with Note(default_x=39.48, default_y=-144.83):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=39.48, default_y=-109.83):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=22.8, default_y=-134.83):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=84.15, default_y=-129.83):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=150.5, default_y=-119.83):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=216.85, default_y=-114.83):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='27', width=276.32):
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=90.0)
            with Note(default_x=15.6, default_y=-139.83):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=15.6, default_y=-104.83):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=38.92, default_y=-109.83):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=97.87, default_y=-119.83):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=156.82, default_y=-114.83):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=215.77, default_y=-129.83):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='28', width=329.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=134.18, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(2)
            with Note(default_x=134.18, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=157.5, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=200.06, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=242.62, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=285.18, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='29', width=251.9):
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=95.0)
            with Note(default_x=19.64, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=19.64, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=147.29, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=147.29, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=45.0, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=96.32, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=167.65, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=198.97, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='30', width=175.0):
            with Note(default_x=24.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=27.32, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=67.54, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=132.82, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Backup():
                Duration(96.0)
            with Note(default_x=14.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='31', width=245.48):
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=100.0)
            with Note(default_x=20.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.94, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=20.36, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=131.94, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=35.36, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=76.51, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=146.94, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=188.09, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='32', width=192.65):
            with Note(default_x=24.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=31.94, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Accidental('sharp')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=27.64, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=76.55, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=147.15, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
        with Measure(number='33', width=392.03):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=105.0)
            with Note(default_x=142.62, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=266.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=163.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=214.48, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Words(' ', default_y=-40.0, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(1)
            with Note(default_x=328.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=2)
            with Backup():
                Duration(96.0)
            with Note(default_x=142.62, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=266.34, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='34', width=244.68):
            with Note(default_x=17.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=110.0)
            with Note(default_x=127.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=32.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=72.51, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=183.01, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.44, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=127.58, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='35', width=311.54):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=13.08, relative_y=30.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('en dehors', relative_x=30.07, relative_y=44.8, font_style='italic', font_size='11')
                Staff(1)
            with Note(default_x=191.54, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=233.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Note(default_x=283.93, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Articulations():
                        DetachedLegato()
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-2.2, relative_y=-44.52):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Words('e cresc. molto', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-84.59, relative_x=25.65)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-84.59, relative_x=25.65)
                Staff(2)
            with Note(default_x=49.93, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Tenuto()
            with Note(default_x=49.93, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=149.55, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=149.55, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=32.12, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(96.0)
                Voice('6')
                Type('whole')
                Accidental('natural')
                Staff(2)
            with Note(default_x=32.12, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(96.0)
                Voice('6')
                Type('whole')
                Staff(2)
            with Note(default_x=32.12, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='36', width=246.12):
            with Note(default_x=28.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        DetachedLegato()
                    NonArpeggiate(type='top', default_x=-25.8, default_y=10.51, relative_x=1.77)
            with Backup():
                Duration(96.0)
            with Note(default_x=50.61, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=50.61, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=191.42, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Tenuto()
            with Note(default_x=191.42, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=28.8, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(96.0)
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    NonArpeggiate(type='bottom', default_x=-14.8, default_y=-9.49, relative_x=-6.6, relative_y=-11.73)
            with Note(default_x=28.8, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Voice('6')
                Type('whole')
                Staff(2)
            with Note(default_x=28.8, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(96.0)
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    NonArpeggiate(type='top', default_x=-14.8, default_y=-9.49, relative_x=-6.6, relative_y=-11.73)
        with Measure(number='37', width=349.64):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.48)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=139.18, default_y=-145.48):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
            with Note(default_x=157.68, default_y=-140.48):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=139.18, default_y=-130.48):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=139.18, default_y=-120.48):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=139.18, default_y=-110.48):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='38', width=249.08):
            with Attributes():
                with Key():
                    Fifths(0)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Plus calme', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', default_y=21.24, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=100.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=7.96, relative_y=-40.0):
                        P()
                        OtherDynamics(' fièrement')
                Staff(2)
                Sound(dynamics=60.0)
            with Note(default_x=118.04, default_y=-110.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=163.55, default_y=-120.48):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=219.04, default_y=-115.48):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='39', width=324.83):
            with Note(default_x=10.94, default_y=-110.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=70.42, default_y=-105.48):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=123.16, default_y=-100.48):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=150.2, default_y=-95.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=193.46, default_y=-100.48):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=236.72, default_y=-95.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=279.97, default_y=-85.48):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=25.58, default_y=-110.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(72.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=236.72, default_y=-115.48):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='40', width=270.82):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=11.8, default_y=-110.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=82.39, default_y=-105.48):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=126.67, default_y=-110.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=187.55, default_y=-100.48):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=241.54, default_y=-95.48):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=32.7, default_y=-115.48):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=126.67, default_y=-120.48):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Staff(2)
        with Measure(number='41', width=366.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(89.97)
            with Note(default_x=64.69, default_y=-114.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=128.51, default_y=-114.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=185.11, default_y=-114.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=215.73, default_y=-114.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=256.87, default_y=-109.97):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=267.84, default_y=-114.97):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=279.55, default_y=-119.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=336.15, default_y=-124.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('Expressif', default_y=-40.0, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=61.37, default_y=-129.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=215.37, default_y=-134.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=66.37, default_y=-149.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(96.0)
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
        with Measure(number='42', width=196.35):
            with Note(default_x=17.32, default_y=-119.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=60.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=17.32, default_y=-134.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=104.53, default_y=-139.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=22.32, default_y=-154.97):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(96.0)
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='43', width=338.13):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Revenir progressivement au Mouvement', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', default_y=21.69, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=95.0)
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=60.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=213.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=256.92, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=309.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=60.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=2, default_y=-75.0)
                Staff(2)
            with Note(default_x=28.32, default_y=-149.97):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=28.32, default_y=-139.97):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
            with Note(default_x=28.32, default_y=-119.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2)
                Staff(2)
        with Measure(number='44', width=293.13):
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', default_y=21.69, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=90.0)
            with Note(default_x=19.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-153.91)
                Staff(1)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('m.g.', default_y=-40.0, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=19.52, default_y=-149.97):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=19.52, default_y=-139.97):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=19.52, default_y=-124.97):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='45', width=336.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(91.29)
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
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
                    Words('T', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=85.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=230.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=267.5, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=312.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=2, default_y=-75.0)
                Staff(2)
            with Note(default_x=72.58, default_y=-151.29):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Tenuto()
            with Note(default_x=72.58, default_y=-141.29):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=72.58, default_y=-121.29):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2)
                Staff(2)
        with Measure(number='46', width=247.69):
            with Note(default_x=19.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-124.72)
                Staff(1)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('m.g.', default_y=-40.0, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=19.52, default_y=-151.29):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=19.52, default_y=-141.29):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=19.52, default_y=-126.29):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(96.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='47', width=279.14):
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('sec.', default_y=11.62, relative_y=20.3, font_style='italic', font_size='11')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-19.46, relative_y=22.93):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=68.38, default_y=-181.29):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=68.38, default_y=-171.29):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=68.38, default_y=-161.29):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('sec.', default_y=63.57, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-21.23, relative_y=18.7):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=197.2, default_y=-186.29):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=197.2, default_y=-176.29):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=197.2, default_y=-166.29):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-72.0)
                Staff(1)
                Sound(tempo=83.0)
        with Measure(number='48', width=330.59):
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=82.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='49', width=337.69):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(66.72)
            with Attributes():
                with Key():
                    Fifths(-6)
            with Direction(placement='above'):
                with DirectionType():
                    Words('au Mouvement ', relative_x=0.88, relative_y=40.34, font_weight='bold', font_size='12')
                with DirectionType():
                    with Metronome(parentheses='no', relative_x=0.88, relative_y=40.34):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-14.15, relative_y=-40.88):
                        Pp()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=134.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=175.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=235.18, default_y=-126.72):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=235.18, default_y=-116.72):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=235.18, default_y=-101.72):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=276.39, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=276.39, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=134.18, default_y=-106.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=134.18, default_y=-96.72):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=175.38, default_y=-111.72):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=175.38, default_y=-101.72):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=276.39, default_y=-101.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='50', width=226.47):
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=54.27, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=83.7, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=125.0, default_y=-111.72):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=125.0, default_y=-101.72):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-106.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-96.72):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=54.27, default_y=-111.72):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=54.27, default_y=-101.72):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=83.7, default_y=-116.72):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=83.7, default_y=-106.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=125.36, default_y=-126.72):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=165.82, default_y=-121.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='51', width=217.72):
            with Note(default_x=11.2, default_y=-101.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=53.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=113.71, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=125.58, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=113.71, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=155.71, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=167.58, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=155.71, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=21.2, default_y=-116.72):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=21.2, default_y=-106.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=65.07, default_y=-106.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=53.2, default_y=-101.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(48.0)
                Voice('6')
                Type('half')
                Staff(2)
        with Measure(number='52', width=207.79):
            with Note(default_x=17.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=29.67, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=56.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=108.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=68.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(48.0)
                Voice('2')
                Type('half')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.8, default_y=-111.72):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=56.88, default_y=-106.72):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=108.93, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=108.93, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
        with Measure(number='53', width=204.69):
            with Note(default_x=18.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=56.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=107.9, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=107.9, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=107.9, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=119.77, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=146.07, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.07, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=146.07, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=146.07, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=18.16, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=18.16, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(48.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='54', width=346.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(72.88)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-84.16)
                Staff(1)
            with Note(default_x=152.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=192.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=236.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=286.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=139.54, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=152.13, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=233.51, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=246.1, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=246.1, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(1)
        with Measure(number='55', width=218.28):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-28.31, relative_y=-37.35):
                        P()
                Staff(1)
                Sound(dynamics=60.0)
            with Note(default_x=47.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=97.56, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=123.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=164.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=190.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=10.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Note(default_x=28.71, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=47.03, default_y=-102.88):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=97.56, default_y=-97.88):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=123.45, default_y=-102.88):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=164.89, default_y=-107.88):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=190.79, default_y=-112.88):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='56', width=200.52):
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim. molto', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-84.26, relative_x=23.88)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-84.26, relative_x=23.88)
                Staff(1)
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=60.08, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=60.08, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=60.08, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=106.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=106.36, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=106.36, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=106.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=152.64, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=152.64, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=152.64, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=60.08, default_y=-107.88):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=152.64, default_y=-112.88):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='57', width=102.63):
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        OtherDynamics('più ')
                        P()
                Staff(1)
                Sound(dynamics=48.89)
            with Note(default_x=55.15, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=55.15, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=55.15, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=55.15, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest(measure='yes')
                Duration(96.0)
                Voice('5')
                Staff(2)
        with Measure(number='58', width=131.23):
            with Note(default_x=17.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=17.44, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=73.35, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=73.35, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=73.35, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=17.44, default_y=-112.88):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=73.35, default_y=-112.88):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(2)
        with Measure(number='59', width=194.76):
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=35.11, default_y=-107.88):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.81, default_y=-102.88):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=48.13, default_y=-112.88):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=78.69, default_y=-122.88):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(72.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=10.0, default_y=-112.88):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Voice('8')
                Type('whole')
                Staff(2)
        with Measure(number='60', width=331.63):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(97.25)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=155.49, default_y=-132.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=266.65, default_y=-127.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=168.51, default_y=-137.25):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=212.27, default_y=-147.25):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(72.0)
                Voice('6')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=130.38, default_y=-137.25):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Voice('8')
                Type('whole')
                Staff(2)
        with Measure(number='61', width=341.88):
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=75.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('lointain', default_y=60.59, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words("En retenant jusqu'à la fin", default_y=31.35, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
            with Note(default_x=52.19, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Note(default_x=72.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=92.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=111.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=146.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('forward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=162.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
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
                    Words('T', default_y=53.49, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=73.0)
            with Note(default_x=197.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=242.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=277.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Note(default_x=297.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
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
                    with Articulations():
                        Staccato()
            with Note(default_x=317.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
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
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=44.44)
            with Note(default_x=16.76, default_y=-122.25):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('m.g.')
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=-55.29)
                Staff(2)
            with Note(default_x=197.25, default_y=-127.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-152.25):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=13.8, default_y=-142.25):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='62', width=178.97):
            with Note(default_x=14.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=39.63, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=55.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=70.0)
            with Note(default_x=71.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.64, default_y=-132.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=106.54, default_y=-127.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=10.68, default_y=-152.25):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=10.68, default_y=-142.25):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='63', width=341.88):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('plus lointain', default_y=69.51, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', default_y=35.3, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=65.0)
            with Note(default_x=52.19, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Note(default_x=72.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=92.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Note(default_x=111.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=146.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('forward hook', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=162.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=197.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=242.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=277.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=297.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
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
                    with Articulations():
                        Staccato()
            with Note(default_x=317.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
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
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(96.0)
            with Note(default_x=16.76, default_y=-122.25):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('m.g.')
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=-55.29)
                Staff(2)
            with Note(default_x=197.25, default_y=-127.25):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-152.25):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=13.8, default_y=-142.25):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='64', width=321.87):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(96.57)
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', default_y=5.0, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=139.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=171.94, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=192.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=212.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=138.82, default_y=-131.57):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none')
                Staff(2)
            with Note(default_x=257.58, default_y=-126.57):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=135.86, default_y=-151.57):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=135.86, default_y=-141.57):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='65', width=334.57):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Lent', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('T', default_y=21.69, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=50.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=89.96, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Tenuto()
            with Note(default_x=101.82, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=122.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=134.03, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=154.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
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
                        Tenuto()
            with Note(default_x=166.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=186.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=198.43, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=236.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=248.72, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=264.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=276.26, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=29.92, default_y=-171.57):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(96.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-151.57):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(96.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-131.57):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(96.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-116.57):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(96.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='66', width=197.27):
            with Note(default_x=11.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=29.92, default_y=-171.57):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(96.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=29.92, default_y=-151.57):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-131.57):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-116.57):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='67', width=171.55):
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(48.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=18.56, relative_y=30.0):
                        Ppp()
                Staff(1)
                Sound(dynamics=27.78)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=74.74)
                Staff(1)
            with Note(default_x=93.64, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=93.64, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(48.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=11.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Tie(type='stop')
                Voice('2')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=29.92, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(96.0)
                Tie(type='stop')
                Voice('2')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(96.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Ppp()
                Staff(2)
                Sound(dynamics=27.78)
            with Note(default_x=11.41, default_y=-176.57):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-171.57):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(96.0)
                Tie(type='start')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-151.57):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-131.57):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-116.57):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='68', width=169.11):
            with Note(default_x=29.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(96.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=29.92, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(96.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Backup():
                Duration(96.0)
            with Note(default_x=11.41, default_y=-176.57):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=29.92, default_y=-171.57):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(96.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=29.92, default_y=-151.57):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(96.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=29.92, default_y=-131.57):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(96.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=29.92, default_y=-116.57):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(96.0)
                Tie(type='stop')
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=385.85):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(-6)
                with Time():
                    Beats('2')
                    BeatType('2')
                with Clef():
                    Sign('G')
                    Line(2)
                with Clef(after_barline='yes'):
                    Sign('F')
                    Line(4)
            with Note(default_x=169.58, default_y=-275.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=223.25, default_y=-280.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=276.91, default_y=-290.0):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=330.58, default_y=-280.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='2', width=230.07):
            with Note(default_x=13.8, default_y=-270.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.47, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.13, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=174.8, default_y=-270.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='3', width=249.92):
            with Note(default_x=10.0, default_y=-255.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=66.08, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.12, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=136.17, default_y=-270.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=192.24, default_y=-250.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
        with Measure(number='4', width=264.4):
            with Note(default_x=10.0, default_y=-255.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=68.3, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=104.75, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=141.19, default_y=-245.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=199.49, default_y=-240.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
        with Measure(number='5', width=358.71):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(76.45)
            with Attributes():
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=130.38, default_y=-256.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=243.56, default_y=-266.45):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(96.0)
            with Note(default_x=142.97, default_y=-261.45):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=187.33, default_y=-266.45):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=256.15, default_y=-271.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=300.52, default_y=-281.45):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='6', width=202.62):
            with Note(default_x=13.44, default_y=-261.45):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=107.05, default_y=-266.45):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-281.45):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=60.24, default_y=-276.45):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=154.22, default_y=-271.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=2)
        with Measure(number='7', width=238.33):
            with Note(default_x=10.0, default_y=-256.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=123.19, default_y=-266.45):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(96.0)
            with Note(default_x=22.59, default_y=-261.45):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=66.95, default_y=-266.45):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.77, default_y=-271.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=180.14, default_y=-281.45):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='8', width=211.74):
            with Note(default_x=13.44, default_y=-261.45):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=111.61, default_y=-271.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-281.45):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=62.52, default_y=-276.45):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=161.06, default_y=-281.45):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=2)
        with Measure(number='9', width=182.96):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Pp()
                Sound(dynamics=44.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-132.27)
            with Note(default_x=10.48, default_y=-251.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
                with Notations():
                    with Articulations():
                        Tenuto()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-286.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=59.98, default_y=-286.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=134.81, default_y=-286.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='10', width=292.68):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=130.86, default_y=-243.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
                with Notations():
                    with Articulations():
                        Tenuto()
            with Backup():
                Duration(96.0)
            with Note(default_x=134.18, default_y=-278.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=177.4, default_y=-278.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
                with Notations():
                    with Articulations():
                        Tenuto()
            with Note(default_x=247.5, default_y=-278.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='11', width=199.36):
            with Note(default_x=10.48, default_y=-243.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-263.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=59.79, default_y=-278.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=105.78, default_y=-263.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=151.77, default_y=-278.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='12', width=222.67):
            with Note(default_x=10.48, default_y=-243.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-263.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=62.57, default_y=-278.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.53, default_y=-263.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=172.3, default_y=-278.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='13', width=239.11):
            with Note(default_x=24.16, default_y=-243.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=27.48, default_y=-263.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=79.99, default_y=-278.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=132.5, default_y=-263.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=185.01, default_y=-278.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='14', width=240.54):
            with Note(default_x=14.48, default_y=-243.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=17.8, default_y=-263.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=73.09, default_y=-278.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=128.37, default_y=-263.21):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=183.66, default_y=-278.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='15', width=313.88):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=140.02, default_y=-246.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=143.34, default_y=-266.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=185.57, default_y=-281.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=227.81, default_y=-266.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=270.05, default_y=-281.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='16', width=207.23):
            with Note(default_x=24.35, default_y=-246.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=27.67, default_y=-266.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=72.16, default_y=-281.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=116.65, default_y=-266.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=161.14, default_y=-281.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='17', width=235.02):
            with Note(default_x=14.48, default_y=-246.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=17.8, default_y=-266.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=64.98, default_y=-281.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.97, default_y=-266.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=171.15, default_y=-281.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='18', width=203.22):
            with Note(default_x=10.48, default_y=-246.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-266.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=60.76, default_y=-281.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=107.71, default_y=-266.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=154.67, default_y=-281.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='19', width=235.02):
            with Note(default_x=14.48, default_y=-246.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=17.8, default_y=-266.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=64.98, default_y=-281.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.97, default_y=-266.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=171.15, default_y=-281.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='20', width=331.66):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=142.06, default_y=-248.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=145.38, default_y=-268.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=191.55, default_y=-283.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=237.72, default_y=-268.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=283.89, default_y=-283.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='21', width=330.09):
            with Note(default_x=24.83, default_y=-248.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=28.15, default_y=-268.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=114.36, default_y=-283.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=196.62, default_y=-268.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=237.21, default_y=-283.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='22', width=203.04):
            with Note(default_x=28.78, default_y=-248.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=32.1, default_y=-268.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=91.87, default_y=-283.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=128.39, default_y=-268.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=164.92, default_y=-283.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='23', width=329.58):
            with Note(default_x=24.32, default_y=-248.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=27.64, default_y=-268.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=113.86, default_y=-283.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=196.12, default_y=-268.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=236.71, default_y=-283.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='24', width=375.98):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=136.22, default_y=-249.83):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=139.54, default_y=-269.83):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=222.42, default_y=-284.83):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=273.08, default_y=-269.83):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=323.73, default_y=-284.83):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='25', width=257.27):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        P()
                Sound(dynamics=60.0)
            with Note(default_x=33.32, default_y=-289.83):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=33.32, default_y=-254.83):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=88.91, default_y=-299.83):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=88.91, default_y=-264.83):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=144.5, default_y=-294.83):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=144.5, default_y=-259.83):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=200.08, default_y=-309.83):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=200.08, default_y=-274.83):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='26', width=284.8):
            with Note(default_x=17.8, default_y=-309.83):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=17.8, default_y=-274.83):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=84.15, default_y=-304.83):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=84.15, default_y=-269.83):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=150.5, default_y=-294.83):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=150.5, default_y=-259.83):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=216.85, default_y=-289.83):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=216.85, default_y=-254.83):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
        with Measure(number='27', width=276.32):
            with Note(default_x=38.92, default_y=-284.83):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=38.92, default_y=-249.83):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=97.87, default_y=-294.83):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=97.87, default_y=-259.83):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=156.82, default_y=-289.83):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=156.82, default_y=-254.83):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=215.77, default_y=-304.83):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=215.77, default_y=-269.83):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='28', width=329.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=157.5, default_y=-295.0):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=157.5, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=200.06, default_y=-290.0):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=200.06, default_y=-255.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=242.62, default_y=-280.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=242.62, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=285.18, default_y=-275.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=285.18, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='29', width=251.9):
            with Note(default_x=45.0, default_y=-270.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=45.0, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=96.32, default_y=-290.0):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=96.32, default_y=-255.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=147.65, default_y=-275.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=147.65, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=198.97, default_y=-285.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=198.97, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
        with Measure(number='30', width=175.0):
            with Note(default_x=27.32, default_y=-280.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=27.32, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=67.54, default_y=-285.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(1)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
            with Note(default_x=67.54, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
            with Note(default_x=132.82, default_y=-280.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=132.82, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='31', width=245.48):
            with Note(default_x=20.72, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=20.72, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=76.51, default_y=-275.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=76.51, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=132.3, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=132.3, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=188.09, default_y=-275.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=188.09, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
        with Measure(number='32', width=192.65):
            with Note(default_x=27.64, default_y=-270.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=27.64, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=76.55, default_y=-280.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Note(default_x=76.55, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Note(default_x=147.15, default_y=-270.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=147.15, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='33', width=392.03):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=142.98, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=142.98, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=204.48, default_y=-270.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=204.48, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Note(default_x=328.56, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=328.56, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='34', width=244.68):
            with Note(default_x=17.8, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=17.8, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=72.51, default_y=-270.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.51, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Note(default_x=183.01, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=183.01, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='35', width=311.54):
            with Note(default_x=35.44, default_y=-280.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=35.44, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.68, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=92.68, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=149.91, default_y=-245.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=149.91, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=233.17, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=233.17, default_y=-195.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
        with Measure(number='36', width=246.12):
            with Note(default_x=32.12, default_y=-210.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=32.12, default_y=-175.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=85.22, default_y=-230.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=85.22, default_y=-195.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=138.32, default_y=-245.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=138.32, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=191.42, default_y=-265.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=191.42, default_y=-230.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='37', width=349.64):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(85.26)
            with Note(default_x=139.18, default_y=-240.74):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Note(default_x=139.18, default_y=-230.74):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Note(default_x=139.18, default_y=-220.74):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(96.0)
            with Note(default_x=142.5, default_y=-300.74):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.5, default_y=-265.74):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=190.72, default_y=-285.74):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=190.72, default_y=-250.74):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=238.95, default_y=-265.74):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=238.95, default_y=-230.74):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=287.18, default_y=-250.74):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=287.18, default_y=-215.74):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='38', width=249.08):
            with Attributes():
                with Key():
                    Fifths(0)
            with Note():
                Rest(measure='yes')
                Duration(96.0)
                Voice('1')
        with Measure(number='39', width=324.83):
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=70.06, default_y=-245.74):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=236.72, default_y=-250.74):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(print_object='no'):
                Rest()
                Duration(24.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=70.42, default_y=-255.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=150.2, default_y=-265.74):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=236.72, default_y=-285.74):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='40', width=270.82):
            with Note(default_x=11.44, default_y=-270.74):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=11.44, default_y=-260.74):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=126.67, default_y=-290.74):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=126.67, default_y=-255.74):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
        with Measure(number='41', width=366.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=64.33, default_y=-279.97):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=215.37, default_y=-284.97):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='42', width=196.35):
            with Note(default_x=20.28, default_y=-284.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
            with Note(default_x=104.53, default_y=-289.97):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='43', width=338.13):
            with Note(default_x=28.32, default_y=-269.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('flat')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=31.64, default_y=-289.97):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=90.99, default_y=-304.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=143.62, default_y=-304.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=170.6, default_y=-289.97):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=256.92, default_y=-304.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='44', width=293.13):
            with Note(default_x=19.52, default_y=-269.97):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Accidental('flat')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(96.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=83.1, default_y=-284.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=136.54, default_y=-284.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=171.01, default_y=-289.97):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=231.27, default_y=-284.97):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='45', width=336.95):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=72.58, default_y=-271.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('flat')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=75.9, default_y=-291.29):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=126.28, default_y=-306.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=170.96, default_y=-306.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=194.22, default_y=-291.29):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=267.5, default_y=-306.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='46', width=247.69):
            with Note(default_x=19.52, default_y=-271.29):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Accidental('flat')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(96.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=71.41, default_y=-286.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(18.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=114.48, default_y=-286.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=148.95, default_y=-291.29):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=197.52, default_y=-286.29):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='47', width=279.14):
            with Note(default_x=20.0, default_y=-301.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=68.38, default_y=-301.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=125.55, default_y=-296.29):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=148.82, default_y=-301.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=197.2, default_y=-301.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=254.37, default_y=-296.29):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='48', width=330.59):
            with Note(default_x=20.0, default_y=-301.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=71.12, default_y=-301.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=116.44, default_y=-296.29):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=139.71, default_y=-301.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=190.83, default_y=-301.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=236.15, default_y=-296.29):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-light')
        with Measure(number='49', width=337.69):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                with Key():
                    Fifths(-6)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=175.38, default_y=-241.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=276.39, default_y=-241.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=134.18, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=175.38, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=211.92, default_y=-271.72):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=235.18, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=276.39, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=312.93, default_y=-271.72):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=2)
        with Measure(number='50', width=226.47):
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=54.27, default_y=-241.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=165.82, default_y=-241.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=13.8, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=54.27, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=102.09, default_y=-271.72):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=125.36, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=165.82, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=201.71, default_y=-271.72):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=2)
        with Measure(number='51', width=217.72):
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=53.2, default_y=-241.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=155.71, default_y=-241.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=11.2, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=53.2, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=90.44, default_y=-271.72):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=113.71, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=155.71, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=192.96, default_y=-271.72):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=2)
        with Measure(number='52', width=207.79):
            with Note(default_x=17.8, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=56.88, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=91.53, default_y=-241.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=119.29, default_y=-206.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=148.37, default_y=-206.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=183.02, default_y=-241.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='53', width=204.69):
            with Note(default_x=18.52, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=56.7, default_y=-276.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=90.55, default_y=-241.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=117.9, default_y=-206.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=146.07, default_y=-206.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=179.93, default_y=-241.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='54', width=346.95):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.07)
            with Note(default_x=152.49, default_y=-282.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=192.62, default_y=-282.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=228.22, default_y=-247.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=246.46, default_y=-212.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=286.59, default_y=-212.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=322.19, default_y=-247.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='55', width=218.28):
            with Note(default_x=43.71, default_y=-252.95):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Note(default_x=43.71, default_y=-232.95):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Note(default_x=43.71, default_y=-217.95):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Voice('1')
                Type('whole')
        with Measure(number='56', width=200.52):
            with Note(default_x=13.8, default_y=-267.95):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-247.95):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=13.8, default_y=-222.95):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=60.08, default_y=-247.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=60.08, default_y=-227.95):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=106.36, default_y=-272.95):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=106.36, default_y=-252.95):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=106.36, default_y=-227.95):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=152.64, default_y=-252.95):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=152.64, default_y=-232.95):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='57', width=102.63):
            with Note():
                Rest()
                Duration(48.0)
                Voice('1')
                Type('half')
            with Note(default_x=55.15, default_y=-242.95):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=55.15, default_y=-222.95):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='58', width=131.23):
            with Note(default_x=17.44, default_y=-262.95):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=17.44, default_y=-242.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Note(default_x=17.44, default_y=-227.95):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=73.35, default_y=-252.95):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=73.35, default_y=-232.95):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='59', width=194.76):
            with Note(default_x=35.11, default_y=-247.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.81, default_y=-242.95):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=48.13, default_y=-252.95):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=78.69, default_y=-262.95):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(72.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=10.0, default_y=-252.95):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('4')
                Type('whole')
        with Measure(number='60', width=331.63):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.05)
            with Note(default_x=155.49, default_y=-273.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=266.65, default_y=-268.31):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(48.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=168.51, default_y=-278.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=212.27, default_y=-288.31):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(2)
                Duration(72.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(96.0)
            with Note(default_x=130.38, default_y=-278.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('4')
                Type('whole')
        with Measure(number='61', width=341.88):
            with Note(default_x=13.8, default_y=-293.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
            with Note(default_x=13.8, default_y=-273.31):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='62', width=178.97):
            with Note(default_x=10.68, default_y=-293.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=10.68, default_y=-273.31):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='63', width=341.88):
            with Note(default_x=13.8, default_y=-293.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
            with Note(default_x=13.8, default_y=-273.31):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='64', width=321.87):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(66.02)
            with Note(default_x=135.86, default_y=-292.59):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=135.86, default_y=-272.59):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='65', width=334.57):
            with Note(default_x=29.92, default_y=-272.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
                    NonArpeggiate(type='bottom', default_x=-32.44, default_y=10.51)
            with Note(default_x=29.92, default_y=-247.59):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(96.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Notations():
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-237.59):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
                    NonArpeggiate(type='top', default_x=-32.44, default_y=10.51)
            with Backup():
                Duration(96.0)
            with Note(default_x=32.88, default_y=-292.59):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(72.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=276.26, default_y=-307.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='66', width=197.27):
            with Note(default_x=29.92, default_y=-272.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-247.59):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-237.59):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=33.24, default_y=-292.59):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=73.85, default_y=-307.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=114.45, default_y=-292.59):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=155.06, default_y=-307.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='67', width=171.55):
            with Note(default_x=29.92, default_y=-272.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-247.59):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=29.92, default_y=-237.59):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(96.0)
            with Note(default_x=32.88, default_y=-292.59):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(48.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=94.0, default_y=-327.59):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
        with Measure(number='68', width=169.11):
            with Note(default_x=29.92, default_y=-292.59):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Voice('1')
                Type('whole')
            with Note(default_x=29.92, default_y=-272.59):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(96.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=29.92, default_y=-247.59):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Accidental('natural')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=29.92, default_y=-237.59):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(96.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(96.0)
            with Note(default_x=33.24, default_y=-327.59):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(1)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(24.0)
                Voice('2')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(2)
                Duration(48.0)
                Voice('2')
                Type('half')
            with Barline(location='right'):
                BarStyle('light-heavy')