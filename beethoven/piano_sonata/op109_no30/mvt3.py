with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Beethoven - Sonata 30, Mvt.3. {Professional production score.}')
    with Identification():
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
            PageHeight(736.565)
            PageWidth(1360.88)
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
        WordFont(font_family='Old Standard TT', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
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
                Volume(100.0)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=248.33):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(15.0)
                        RightMargin(0.0)
                    TopSystemDistance(84.17)
                with StaffLayout(number=2):
                    StaffDistance(86.95)
            with Attributes():
                Divisions(40.0)
                with Key():
                    Fifths(4)
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
                    with Metronome(parentheses='no', default_x=-41.8, default_y=71.97, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('35')
                Staff(1)
                Sound(tempo=35.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Andante  molto  cantabile  ed  espressivo.', enclosure='rectangle', default_y=6.57, relative_x=-30.0, relative_y=40.0, font_weight='bold', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Gesangvoll,  mit  innigster  Empfindung.', enclosure='rectangle', default_y=11.17, relative_x=-35.0, relative_y=70.0, font_weight='bold', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-54.2, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Direction(placement='below'):
                with DirectionType():
                    Words('mezza voce', enclosure='rectangle', default_y=-46.0, relative_y=-40.0, font_weight='bold', font_style='italic')
                Staff(1)
            with Note(default_x=136.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=165.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=213.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=136.52, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=165.66, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=194.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=136.52, default_y=-176.95):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=165.66, default_y=-166.95):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=194.8, default_y=-161.95):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='2', width=93.8):
            with Note(default_x=15.8, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=41.27, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=41.27, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=53.43, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-156.95):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=41.27, default_y=-151.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=66.73, default_y=-146.95):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='3', width=134.38):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-64.2, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=47.52, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=99.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=15.8, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=47.52, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=79.23, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-141.95):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=47.52, default_y=-131.95):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=79.23, default_y=-126.95):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=127.33):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-95.71)
                Staff(1)
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=43.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=75.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=43.9, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=43.9, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=75.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=75.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-121.95):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=43.9, default_y=-136.95):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=75.8, default_y=-156.95):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=102.58, default_y=-161.95):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=182.78):
            with Note(default_x=15.8, default_y=-55.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(3)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=24.0, default_y=-40.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=32.2, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=41.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=5.84)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-60.71, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-91.65)
                Staff(1)
            with Note(default_x=89.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=142.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-6.82)
                Staff(1)
            with Note(default_x=158.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=89.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=119.94, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=41.14, default_y=-166.95):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=89.12, default_y=-131.95):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=119.94, default_y=-161.95):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(120.0)
            with Note(default_x=57.3, default_y=-166.95):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(80.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Forward():
                Duration(40.0)
        with Measure(number='6', width=127.34):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.42, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=40.47, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=63.73, default_y=-60.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(3)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=71.93, default_y=-55.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(3)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.12, default_y=-60.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(3)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('begin', number=3)
            with Note(default_x=88.32, default_y=-65.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=97.27, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-156.95):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=12.0, default_y=-136.95):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=40.47, default_y=-151.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=40.47, default_y=-141.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=97.27, default_y=-146.95):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=97.27, default_y=-136.95):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=151.38):
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='Old Standard TT', font_size='10', font_weight='bold', font_style='italic', default_y=-92.12)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-92.12)
                Staff(1)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=43.88, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=93.62, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-141.95):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=43.88, default_y=-141.95):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(80.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(40.0)
            with Note(default_x=43.88, default_y=-186.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=43.88, default_y=-151.95):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.06, default_y=-186.95):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(40.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=76.06, default_y=-151.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(40.0)
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=167.16):
            with Attributes():
                with Clef(number=1):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-62.12, relative_x=6.64, relative_y=-30.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-87.12)
                Staff(1)
            with Note(default_x=24.08, default_y=0.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=90.63, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
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
                Duration(120.0)
            with Note(default_x=36.24, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=64.06, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=90.63, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=24.08, default_y=-176.95):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.06, default_y=-166.95):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=90.63, default_y=-156.95):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=24.08, default_y=-186.95):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(80.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=90.63, default_y=-191.95):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(40.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=253.54):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(15.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(81.7)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Clef(number=1):
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=137.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=164.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=218.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=164.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=201.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=137.62, default_y=-116.7):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=164.14, default_y=-141.7):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=164.14, default_y=-116.7):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=201.65, default_y=-136.7):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=201.65, default_y=-116.7):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=113.57):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=37.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=78.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=37.24, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=62.48, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-131.7):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=12.0, default_y=-116.7):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=37.24, default_y=-146.7):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=37.24, default_y=-116.7):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=62.48, default_y=-141.7):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=62.48, default_y=-116.7):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=121.17):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-80.4)
                Staff(1)
            with Note(default_x=42.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=85.85, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=42.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=69.17, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-136.7):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=15.8, default_y=-116.7):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=42.49, default_y=-151.7):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=42.49, default_y=-116.7):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=69.17, default_y=-146.7):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=69.17, default_y=-111.7):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=101.81):
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=12.0, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=60.0)
            with Note(default_x=42.02, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=42.02, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-7.79)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=71.11, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.11, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=0.97)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-141.7):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=12.0, default_y=-116.7):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=42.02, default_y=-141.7):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=42.02, default_y=-121.7):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=71.11, default_y=-161.7):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.11, default_y=-126.7):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='13', width=156.25):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='Old Standard TT', font_size='10', font_weight='bold', font_style='italic', default_y=-70.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-70.0)
                Staff(1)
            with Note(default_x=24.12, default_y=-60.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(3)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=32.32, default_y=-50.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=40.52, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=49.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=80.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=131.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=49.46, default_y=-166.7):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=49.46, default_y=-131.7):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=80.71, default_y=-131.7):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=80.71, default_y=-121.7):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=99.8, default_y=-136.7):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=111.96, default_y=-131.7):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=111.96, default_y=-121.7):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=225.29):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-41.8, relative_x=3.32, relative_y=-30.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-91.45)
                Staff(1)
            with Note(default_x=100.65, default_y=-45.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=111.61, default_y=-35.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=122.57, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=134.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=166.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=183.76, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=183.76, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=200.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=200.53, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-19.48)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=42.0, default_y=-141.7):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Tie(type='start')
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tied(type='start')
            with Note(default_x=57.96, default_y=-131.7):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Tie(type='start')
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='start')
            with Note(default_x=73.92, default_y=-121.7):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(3)
                Tie(type='start')
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Tied(type='start')
            with Note(default_x=89.88, default_y=-116.7):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(3)
                Tie(type='start')
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Tied(type='start')
            with Note(default_x=134.28, default_y=-141.7):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(80.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=134.28, default_y=-131.7):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(80.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=122.12, default_y=-121.7):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(80.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=134.28, default_y=-116.7):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(80.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=183.76, default_y=-141.7):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=183.76, default_y=-131.7):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=171.6, default_y=-121.7):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=183.76, default_y=-116.7):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=200.53, default_y=-136.7):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=200.53, default_y=-126.7):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=200.53, default_y=-116.7):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=136.72):
            with Direction(placement='below'):
                with DirectionType():
                    Words('mezza voce', enclosure='rectangle', default_y=-48.5, relative_y=-30.0, font_weight='bold', font_style='italic')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-42.95, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=52.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=101.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=52.68, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=80.89, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest()
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=52.68, default_y=-126.7):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=80.89, default_y=-131.7):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-151.7):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(80.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=80.89, default_y=-151.7):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=124.15):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=58.89, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=58.89, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=58.89, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-171.7):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.35, default_y=-151.7):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=58.89, default_y=-136.7):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=285.85):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(15.0)
                        RightMargin(0.0)
                    TopSystemDistance(108.2)
                with StaffLayout(number=2):
                    StaffDistance(70.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.96, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-84.11, default_y=96.0, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('45')
                Staff(1)
                Sound(tempo=45.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('VAR.  I.', enclosure='rectangle', relative_x=-85.0, relative_y=75.0, font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('molto espressivo.', enclosure='rectangle', default_y=60.2, relative_x=-65.0, relative_y=45.0, font_weight='bold')
                Staff(1)
            with Note(default_x=159.82, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=178.83, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=235.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=261.09, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=178.83, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=207.33, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=207.33, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=207.33, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=207.33, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=235.82, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=235.82, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=235.82, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=235.82, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=144.53):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=48.42, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=84.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(35.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Dot()
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=119.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                Beam('backward hook', number=3)
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=48.42, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=48.42, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=36.27, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=48.42, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=84.85, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=84.85, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.69, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=84.85, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='19', width=222.44):
            with Note(default_x=13.75, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=32.77, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=81.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=103.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=118.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=134.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=150.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=165.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('end', number=3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=181.45, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.68, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=32.77, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=59.85, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.85, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.85, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.85, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=103.16, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=103.16, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=103.16, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=103.16, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='20', width=107.71):
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='Old Standard TT', font_size='10', font_weight='bold', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=82.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-145.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=39.03, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=39.03, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=39.03, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=39.03, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=66.06, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=66.06, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=66.06, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=66.06, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=151.64):
            with Note(default_x=13.75, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=32.77, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=81.42, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=101.9, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=126.88, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(120.0)
            with Note(default_x=32.77, default_y=-150.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=60.93, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.93, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.93, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.93, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=101.9, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=101.9, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=101.9, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=101.9, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=139.03):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=32.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=73.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=93.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=114.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-155.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=52.91, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=52.91, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=52.91, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=52.91, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=93.82, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=93.82, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='23', width=181.31):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=41.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.66, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=98.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=128.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=154.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(80.0)
            with Note(default_x=128.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=66.66, default_y=-140.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=128.85, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-160.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(40.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=66.66, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=98.83, default_y=-165.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(20.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=128.85, default_y=-170.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=154.28, default_y=-180.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(20.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='24', width=339.22):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(15.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(91.58)
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=56.29)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=122.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=151.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=178.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.04, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=236.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=236.06, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=298.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=122.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(80.0)
            with Note(default_x=122.68, default_y=-191.58):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=151.06, default_y=-171.58):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=178.55, default_y=-176.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=206.04, default_y=-181.58):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=236.06, default_y=-196.58):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=236.06, default_y=-176.58):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=263.55, default_y=-191.58):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=298.97, default_y=-186.58):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=122.68, default_y=-211.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(80.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(40.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='25', width=198.65):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=56.22)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=17.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=72.81, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=99.88, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=129.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=129.9, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=173.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=17.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(80.0)
            with Note(default_x=17.36, default_y=-191.58):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.74, default_y=-171.58):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=72.81, default_y=-176.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=99.88, default_y=-181.58):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=129.9, default_y=-196.58):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=129.9, default_y=-176.58):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=156.97, default_y=-191.58):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=156.97, default_y=-181.58):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(120.0)
            with Note(default_x=17.36, default_y=-211.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(80.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(40.0)
        with Measure(number='26', width=152.0):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=4.75, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=23.77, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-8.77)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=73.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=65.56)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=2, default_y=-75.0)
                Staff(1)
            with Note(default_x=103.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-9.74)
                Staff(1)
            with Note(default_x=128.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-4.87)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=23.77, default_y=-186.58):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=23.77, default_y=-176.58):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=52.48, default_y=-151.58):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.48, default_y=-141.58):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=52.48, default_y=-126.58):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=103.38, default_y=-146.58):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=103.38, default_y=-136.58):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=103.38, default_y=-121.58):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                Ending(None, number='2', type='stop')
        with Measure(number='27', width=199.62):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
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
            with Note(default_x=29.1, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=63.03, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-12.66)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=110.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=65.56)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=2, default_y=-75.0)
                Staff(1)
            with Note(default_x=150.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-27.27)
                Staff(1)
            with Note(default_x=174.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-18.83)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=63.03, default_y=-176.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=90.29, default_y=-141.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=90.29, default_y=-131.58):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=150.69, default_y=-151.58):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=150.69, default_y=-141.58):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=150.69, default_y=-126.58):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='28', width=155.5):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=13.75, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=33.27, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=106.57, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=130.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(80.0)
            with Note(default_x=106.57, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(120.0)
            with Note(default_x=33.27, default_y=-181.58):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=60.53, default_y=-146.58):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.53, default_y=-136.58):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.53, default_y=-126.58):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=106.57, default_y=-156.58):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=106.57, default_y=-121.58):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='29', width=187.51):
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='Old Standard TT', font_size='10', font_weight='bold', font_style='italic', default_y=-87.26)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-87.26)
                Staff(1)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=15.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=42.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=42.78, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=69.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=99.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(2.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('double-sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=126.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=158.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(40.0)
            with Note(default_x=69.76, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=99.78, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=126.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=158.94, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(20.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-121.58):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=42.78, default_y=-126.58):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=69.76, default_y=-126.58):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=99.78, default_y=-131.58):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=126.76, default_y=-171.58):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=126.76, default_y=-136.58):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=158.94, default_y=-176.58):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=158.94, default_y=-141.58):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-151.58):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=69.76, default_y=-151.58):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Forward():
                Duration(40.0)
        with Measure(number='30', width=245.46):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(15.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(71.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=3.32, relative_y=-30.0):
                        Sf()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=114.32, default_y=10.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=133.34, default_y=45.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=77.78)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-65.0)
                Staff(1)
            with Note(default_x=177.98, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=197.44, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=220.7, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=133.34, default_y=-156.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=159.18, default_y=-121.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=159.18, default_y=-111.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=197.44, default_y=-136.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=197.44, default_y=-126.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=197.44, default_y=-111.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='31', width=184.36):
            with Note(default_x=21.16, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.83, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.09, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=99.75, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-0.97)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=95.56)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-63.35)
                Staff(1)
            with Note(default_x=131.93, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=159.6, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-0.55)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=21.16, default_y=-166.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=72.09, default_y=-131.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.09, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.93, default_y=-111.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.09, default_y=-106.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=131.93, default_y=-126.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=131.93, default_y=-116.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=131.93, default_y=-106.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='32', width=246.84):
            with Direction(placement='below'):
                with DirectionType():
                    Words('mezza voce', enclosure='rectangle', default_y=-40.0, relative_y=-15.0, font_weight='bold', font_style='italic')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=13.75, default_y=5.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=32.77, default_y=40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=50.18, default_y=5.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=69.19, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=96.86, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(10.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=120.12, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=143.38, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=171.05, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(10.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=194.31, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=217.57, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(120.0)
            with Note(default_x=32.77, default_y=-141.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=96.86, default_y=-116.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=96.86, default_y=-106.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=96.86, default_y=-91.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=171.05, default_y=-121.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=158.89, default_y=-111.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=171.05, default_y=-106.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=171.05, default_y=-96.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='33', width=206.06):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=51.68)
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.22, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=76.35, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(10.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=99.61, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=115.32, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='Old Standard TT', font_size='10', font_weight='bold', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=140.46, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=181.3, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-161.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=64.19, default_y=-126.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.35, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=64.19, default_y=-111.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.35, default_y=-106.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.35, default_y=-96.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=140.46, default_y=-126.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.46, default_y=-116.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=140.46, default_y=-106.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=140.46, default_y=-91.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=165.59, default_y=-131.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=165.59, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=165.59, default_y=-106.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=165.59, default_y=-96.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='34', width=174.65):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-65.0)
                Staff(1)
            with Note(default_x=13.75, default_y=0.0):
                Grace(slash='yes')
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=32.77, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-8.77)
                Staff(1)
            with Note(default_x=80.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=65.56)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-66.16)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-66.16)
                Staff(1)
            with Note(default_x=110.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=4.23)
                Staff(1)
            with Note(default_x=134.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-13.52)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=32.77, default_y=-166.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=60.16, default_y=-131.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.16, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.16, default_y=-106.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=110.1, default_y=-126.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=110.1, default_y=-116.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=110.1, default_y=-101.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='35', width=175.14):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=54.15)
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.22, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=13.34, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('30')
                Staff(1)
                Sound(tempo=30.0)
            with Note(default_x=74.48, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(10.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=97.74, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.93, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('20')
                Staff(1)
                Sound(tempo=20.0)
            with Note(default_x=113.4, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=135.35, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-161.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=62.32, default_y=-126.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=74.48, default_y=-121.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=62.32, default_y=-111.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=74.48, default_y=-106.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=74.48, default_y=-96.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=135.35, default_y=-126.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=135.35, default_y=-116.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=135.35, default_y=-106.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=135.35, default_y=-91.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='stop')
        with Measure(number='36', width=476.51):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(15.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(70.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('50')
                Staff(1)
                Sound(tempo=50.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='37', width=378.0):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='38', width=378.0):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='39', width=476.51):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(15.0)
                        RightMargin(0.0)
                    SystemDistance(126.5)
                with StaffLayout(number=2):
                    StaffDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='40', width=378.0):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='41', width=378.0):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='42', width=136.32):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(15.0)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='43', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='44', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='45', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='46', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='47', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='48', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='49', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='50', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='51', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='52', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='53', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='54', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='55', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='56', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='57', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='58', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='59', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='60', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='61', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='62', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='63', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='64', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='65', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='66', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='67', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='68', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='69', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='70', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='71', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='72', width=136.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(15.0)
                        RightMargin(-0.0)
                    SystemDistance(126.5)
                with StaffLayout(number=2):
                    StaffDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='73', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='74', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='75', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='76', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='77', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='78', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='79', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='80', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='81', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='82', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='83', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='84', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='85', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='86', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='87', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='88', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='89', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='90', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='91', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='92', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='93', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='94', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='95', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='96', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='97', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='98', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='99', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='100', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='101', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='102', width=136.32):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(15.0)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='103', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='104', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='105', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='106', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='107', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='108', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='109', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='110', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='111', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='112', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='113', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='114', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='115', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='116', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='117', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='118', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='119', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='120', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='121', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='122', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='123', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='124', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='125', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='126', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='127', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='128', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='129', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='130', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='131', width=37.8):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='132', width=202.42):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(15.0)
                        RightMargin(710.39)
                    SystemDistance(126.5)
                with StaffLayout(number=2):
                    StaffDistance(70.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='133', width=103.9):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='134', width=103.9):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
        with Measure(number='135', width=111.9):
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                Rest(measure='yes')
                Duration(120.0)
                Voice('5')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')