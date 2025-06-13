with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('6 Minuets')
    with Identification():
        Creator('Ludwig van Beethoven', type='composer')
        Rights('Public Domain (PianoXML typeset)')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-14')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
        Source('http://musescore.com/user/9292486/scores/5881998')
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
        CreditWords('6 Minuets', default_x=671.547, default_y=1834.6, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('WoO 10', default_x=671.547, default_y=1770.66, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Ludwig van Beethoven', default_x=1279.16, default_y=1734.6, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Public Domain (PianoXML typeset)', default_x=671.547, default_y=127.877, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Public Domain (PianoXML typeset)', default_x=671.547, default_y=127.877, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Public Domain (PianoXML typeset)', default_x=671.547, default_y=127.877, justify='center', valign='bottom', font_size='8')
    with Credit(page=4):
        CreditType('rights')
        CreditWords('Public Domain (PianoXML typeset)', default_x=671.547, default_y=127.877, justify='center', valign='bottom', font_size='8')
    with Credit(page=5):
        CreditType('rights')
        CreditWords('Public Domain (PianoXML typeset)', default_x=671.547, default_y=127.877, justify='center', valign='bottom', font_size='8')
    with Credit(page=6):
        CreditType('rights')
        CreditWords('Public Domain (PianoXML typeset)', default_x=671.547, default_y=127.877, justify='center', valign='bottom', font_size='8')
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
        with Measure(number='1', width=221.91):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(70.85)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(69.63)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
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
                    with Dynamics(default_x=6.58, default_y=-43.89, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=86.23, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=119.75, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.27, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.79, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=86.23, default_y=-134.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=119.75, default_y=-139.63):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.27, default_y=-134.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.79, default_y=-139.63):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='2', width=196.22):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=74.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=134.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=134.35, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=134.35, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-134.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=74.07, default_y=-134.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=134.35, default_y=-134.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=134.35, default_y=-99.63):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=267.75):
            with Note(default_x=13.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=13.44, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.61, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=145.98, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=176.02, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.11, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-134.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-99.63):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=79.89, default_y=-169.63):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=79.89, default_y=-134.63):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=145.98, default_y=-134.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=176.02, default_y=-139.63):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.07, default_y=-134.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.11, default_y=-139.63):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='4', width=200.59):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=75.53, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.35, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=137.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=137.26, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=137.26, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-134.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=75.53, default_y=-134.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=137.26, default_y=-134.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=137.26, default_y=-99.63):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=257.89):
            with Note(default_x=13.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=13.44, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=13.44, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.25, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=140.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=170.11, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.84, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-134.63):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-99.63):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.0, default_y=-169.63):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=77.0, default_y=-134.63):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=140.21, default_y=-114.63):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=170.11, default_y=-119.63):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.84, default_y=-114.63):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.57, default_y=-119.63):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='6', width=197.61):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(118.42)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=106.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=151.13, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(36.0)
            with Note(default_x=61.37, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=106.25, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=151.13, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='7', width=158.77):
            with Note(default_x=13.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=61.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=61.59, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=61.59, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=61.59, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=109.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.38, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=109.38, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=109.38, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-75.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=61.59, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=61.59, default_y=-80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=109.38, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.38, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=203.86):
            with Note(default_x=21.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=10.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=21.87, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=21.87, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=70.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=70.57, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=113.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=113.76, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=135.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=135.9, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=179.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=179.1, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=21.87, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=21.87, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=70.57, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=70.57, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=135.9, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=135.9, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='9', width=114.55):
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=10.0, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=10.0, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=52.95, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='10', width=135.88):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.59, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=54.49, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.09, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='11', width=158.77):
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=61.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=61.59, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=61.59, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=109.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=109.38, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=109.38, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=61.59, default_y=-170.0):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=61.59, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=109.38, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=109.38, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='12', width=224.92):
            with Note(default_x=10.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=10.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=10.36, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=117.71, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=150.38, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.69, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.01, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=10.72, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=64.22, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=64.22, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=117.71, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=117.71, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=252.1):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(118.42)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=80.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=80.98, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=69.11, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=80.98, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=137.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=137.48, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=125.62, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=137.48, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=193.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=193.99, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=182.13, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=193.99, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=80.98, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=80.98, default_y=-80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=137.48, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=137.48, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=193.99, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=193.99, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=225.56):
            with Note(default_x=22.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=22.95, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=10.36, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=22.95, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=128.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=152.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=23.31, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=23.31, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=75.86, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=75.86, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=128.41, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=128.41, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='15', width=157.64):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=61.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=108.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=108.62, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=61.21, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=108.62, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='16', width=175.12):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=67.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=67.04, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=120.28, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=120.28, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=67.04, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=120.28, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='17', width=255.74):
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=139.87, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=168.43, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.0, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.57, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.16, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=14.16, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=14.16, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=14.16, default_y=-80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.01, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.01, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.01, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=77.01, default_y=-80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.87, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.87, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.87, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.87, default_y=-80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=128.21):
            with Note(default_x=13.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=61.68, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Fine', relative_y=20.0)
                Sound(fine='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='19', width=132.07):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(118.42)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Trio', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=83.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='20', width=222.97):
            with Note(default_x=10.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=116.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=151.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=186.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=45.83, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=80.94, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=116.05, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.16, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=186.26, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='21', width=219.26):
            with Note(default_x=10.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=45.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=79.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=114.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=45.21, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=79.7, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=114.19, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=148.68, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.17, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='22', width=206.61):
            with Note(default_x=10.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=57.04, default_y=-10.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=75.48, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=140.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=172.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=43.1, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=75.48, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=107.86, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=140.25, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=172.63, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='23', width=213.02):
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=144.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=43.57, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=77.14, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=110.71, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=144.28, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=177.85, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='24', width=200.45):
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=106.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=137.17, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=168.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=44.64, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=75.48, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.32, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.17, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.01, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='25', width=267.81):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(-0.0)
                    SystemDistance(118.42)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=197.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=232.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=61.37, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=95.51, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=129.65, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.79, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=197.93, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=232.07, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='26', width=238.25):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=84.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=155.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=213.49, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=49.3, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=84.8, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=120.3, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=155.8, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.3, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='27', width=134.95):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=65.05, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='28', width=80.53):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='29', width=256.4):
            with Note(default_x=17.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=17.23, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=56.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=56.83, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=96.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=96.42, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=136.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=136.01, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=175.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=175.61, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=215.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=215.2, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=17.23, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=56.83, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=96.42, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=136.01, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=175.61, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=215.2, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='30', width=216.44):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=44.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=78.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=112.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=146.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=180.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='31', width=255.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(118.42)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=61.37, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=93.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.51, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=125.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=125.64, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=157.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=157.78, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=189.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=189.91, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=222.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=222.05, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=61.37, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.51, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=125.64, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=157.78, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=189.91, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=222.05, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='32', width=219.18):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=44.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=79.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=113.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=182.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='33', width=191.76):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=100.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=130.11, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=160.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=10.0, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=40.03, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=70.05, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=100.08, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=130.11, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.14, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='34', width=195.56):
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=73.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=103.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=133.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=13.8, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=43.83, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=73.85, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=103.88, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.91, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.94, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='35', width=213.58):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=138.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=188.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=44.91, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=76.03, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=107.14, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=138.25, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.37, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='36', width=118.5):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=56.82, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D.C. al Fine', relative_y=20.0)
                Sound(dacapo='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='1', width=172.58):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(70.85)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(1)
                with Time():
                    Beats('3')
                    BeatType('4')
                Staves(2)
            with Note(default_x=103.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=103.21, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=147.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=147.81, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='2', width=241.92):
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=10.0, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=60.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=60.76, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=86.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=86.77, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=137.53, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=137.53, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=163.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=163.55, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=214.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=214.31, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=86.77, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=163.55, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=175.39):
            with Note(default_x=10.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=10.36, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=107.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=107.64, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=150.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=150.62, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.18, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='4', width=163.02):
            with Note(default_x=14.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=14.36, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=100.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=100.31, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=138.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=138.25, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.72, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=57.51, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='5', width=163.38):
            with Note(default_x=14.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=14.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=100.33, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=100.33, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=138.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=138.61, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=57.17, default_y=-180.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='6', width=228.09):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=10.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=57.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=57.71, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=82.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=82.16, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=129.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=129.87, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=154.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=154.33, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=202.03, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=202.03, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=82.16, default_y=-135.0):
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
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-30.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=154.33, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=230.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(132.7)
                with StaffLayout(number=2):
                    StaffDistance(89.01)
            with Note(default_x=81.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=81.21, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=172.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=172.43, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=200.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=200.82, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=81.57, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=127.0, default_y=-139.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=172.43, default_y=-134.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=216.01):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=10.0, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=44.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=44.07, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=78.14, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=78.14, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=112.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=112.21, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=146.27, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=146.27, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=180.34, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.34, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-129.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=146.27, default_y=-164.01):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=117.04):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-149.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=54.19, default_y=-114.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='10', width=89.28):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=56.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='11', width=162.51):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=62.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=62.84, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=111.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=111.87, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-124.01):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-114.01):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=62.84, default_y=-129.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=62.84, default_y=-114.01):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=111.87, default_y=-134.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=111.87, default_y=-114.01):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=209.5):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=115.58, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=138.64, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-114.01):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.16, default_y=-139.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=64.87, default_y=-149.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=115.58, default_y=-139.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=169.2):
            with Note(default_x=10.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=10.72, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=57.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=57.04, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=103.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.36, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=144.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=144.44, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-134.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=103.36, default_y=-154.01):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='14', width=275.13):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(132.7)
                with StaffLayout(number=2):
                    StaffDistance(74.19)
            with Note(default_x=81.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=81.21, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=131.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=131.83, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=205.47, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=205.47, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=250.36, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=250.36, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=81.21, default_y=-134.19):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='15', width=272.37):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-50.66, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=13.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=13.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=70.43, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=70.43, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=99.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=99.46, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=156.09, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=156.09, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=185.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=185.11, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=241.74, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=241.74, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-189.19):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-154.19):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=99.46, default_y=-179.19):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=99.46, default_y=-144.19):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=185.11, default_y=-169.19):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=185.11, default_y=-134.19):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='16', width=208.87):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=10.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-46.51, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=128.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=128.22, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=180.49, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.49, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-154.19):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=10.36, default_y=-119.19):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-34.15):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=69.29, default_y=-159.19):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=69.29, default_y=-124.19):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=128.22, default_y=-164.19):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=128.22, default_y=-129.19):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=209.65):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-51.43, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=130.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=130.22, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=181.68, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=181.68, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.16, default_y=-164.19):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=14.16, default_y=-129.19):
                Chord()
                with Pitch():
                    Step('E')
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
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.47):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=72.19, default_y=-164.19):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=72.19, default_y=-129.19):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=130.22, default_y=-169.19):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=130.22, default_y=-134.19):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='18', width=125.27):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=66.19)
            with Note(default_x=13.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-154.19):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=60.21, default_y=-119.19):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='19', width=103.07):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=66.19)
            with Note(default_x=13.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=13.8, default_y=-154.19):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=62.21, default_y=-119.19):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Fine', relative_y=20.0)
                Sound(fine='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='stop')
        with Measure(number='20', width=212.1):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(132.7)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Trio', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=109.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=143.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=176.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(18.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='21', width=181.57):
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=38.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=66.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=94.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=123.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=151.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=66.66, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=123.32, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=181.57):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=38.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
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
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=94.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=123.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=151.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=66.66, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=123.32, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=197.94):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=41.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=72.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=103.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=134.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=72.11, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=134.23, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='24', width=210.59):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=43.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=76.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=175.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.33, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=142.66, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='25', width=210.59):
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=43.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=76.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=175.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.33, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=142.66, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=229.7):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(132.7)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=81.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=105.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=130.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=154.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=179.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=203.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=81.21, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=130.17, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=179.14, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='27', width=187.96):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=38.53, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=67.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=95.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=129.3, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=157.83, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=129.3, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='28', width=85.61):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=10.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='29', width=114.34):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=23.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=53.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=83.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(18.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='30', width=202.46):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=41.11, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=72.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=103.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=138.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=103.33, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=138.64, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.75, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=197.51):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=45.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=75.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=105.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=135.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.87, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=75.88, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=105.88, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=135.89, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=165.9, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='32', width=176.78):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=42.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=121.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=42.07, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.69, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.31, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=121.93, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=148.55, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='33', width=282.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(132.7)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=81.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=114.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=147.63, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=214.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=247.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=81.21, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=114.42, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=147.63, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.83, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=214.04, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=247.25, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='34', width=194.47):
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=70.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=101.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=131.92, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=162.4, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=70.96, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=131.92, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='35', width=220.83):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.87, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=79.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=114.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=149.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=184.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=79.74, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=149.49, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(36.0)
            with Note(default_x=26.17, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='36', width=224.21):
            with Note(default_x=10.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=46.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=81.35, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=116.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=151.98, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=187.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=81.35, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=151.98, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='37', width=126.24):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=66.64)
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=71.51, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(18.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=71.51, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(18.0)
            with Note(default_x=13.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='38', width=146.56):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=66.64)
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=68.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=68.09, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Forward():
                Duration(6.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D.C. al Fine', relative_y=20.0)
                Sound(dacapo='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='stop')
        with Measure(number='1', width=203.9):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(70.85)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
                with Time():
                    Beats('3')
                    BeatType('4')
                Staves(2)
            with Note(default_x=122.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=175.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='2', width=222.38):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=10.0, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=144.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=194.81, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=10.36, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=61.03, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=61.03, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=87.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=87.0, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='3', width=222.74):
            with Note(default_x=10.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=10.36, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=144.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=195.17, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=10.72, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=61.39, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=61.39, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=87.36, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=87.36, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='4', width=283.52):
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=173.75, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=200.79, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.16, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=14.16, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=66.92, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=66.92, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=93.96, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=93.96, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=146.71, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=146.71, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=173.75, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=173.75, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=254.87, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=254.87, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=211.84):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=139.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=186.26, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='6', width=262.87):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(138.05)
                with StaffLayout(number=2):
                    StaffDistance(71.49)
            with Note(default_x=104.18, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=177.11, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=205.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=233.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(36.0)
            with Note(default_x=104.18, default_y=-176.49):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=104.18, default_y=-141.49):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=149.06, default_y=-141.49):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=149.06, default_y=-106.49):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='7', width=187.65):
            with Note(default_x=10.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=40.12, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=69.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=98.49, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=127.68, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=156.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(36.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=98.49, default_y=-141.49):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=127.68, default_y=-126.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=156.86, default_y=-116.49):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='8', width=155.54):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=10.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=48.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=48.2, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=67.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=67.78, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=110.86, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=110.86, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=110.86, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-106.49):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=110.86, default_y=-141.49):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='9', width=112.21):
            with Note(default_x=13.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-126.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=53.68, default_y=-161.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='10', width=93.4):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=68.64, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='11', width=182.34):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=10.0, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=66.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=66.91, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=123.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.83, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-136.49):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.46, default_y=-126.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=66.91, default_y=-141.49):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.37, default_y=-126.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=123.83, default_y=-146.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=152.28, default_y=-126.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='12', width=200.35):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=10.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=127.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=175.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-151.49):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.44, default_y=-126.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.88, default_y=-126.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.31, default_y=-126.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=127.75, default_y=-126.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=157.19, default_y=-126.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='13', width=286.14):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(138.05)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=100.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=100.38, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=161.77, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=161.77, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=223.15, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=223.15, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=100.38, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=131.07, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=161.77, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=192.46, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=223.15, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=253.85, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='14', width=213.78):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=10.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=137.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=189.01, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.82, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=73.65, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=105.47, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.3, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.12, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='15', width=203.26):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=21.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=21.87, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=105.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=137.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=169.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(36.0)
            with Note(default_x=21.87, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=21.87, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=21.87, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=73.23, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=73.23, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=61.37, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=73.23, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='16', width=201.07):
            with Note(default_x=10.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=42.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=73.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=105.2, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=136.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=168.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(36.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=105.2, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=136.62, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=168.05, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='17', width=168.97):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=10.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=51.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=51.77, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=73.17, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=73.17, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=120.27, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=120.27, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=120.27, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=120.27, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='18', width=121.16):
            with Note(default_x=13.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=58.15, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Fine', relative_y=20.0)
                Sound(fine='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='19', width=171.18):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(138.05)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Trio', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=125.23, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='20', width=212.19):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=28.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=29.02, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=59.28, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.54, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=119.8, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.07, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=180.33, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(36.0)
            with Note(default_x=29.02, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=89.54, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=150.07, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=203.13):
            with Note(default_x=10.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=55.88, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=74.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=106.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=137.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.35, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=10.72, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=42.52, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=74.33, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.13, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.93, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.73, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='22', width=211.55):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=135.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=186.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=10.36, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.73, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=73.09, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=104.45, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=135.82, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=167.18, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=73.09, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=135.82, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=203.13):
            with Note(default_x=10.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=55.88, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=74.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=106.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=137.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.35, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=10.72, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=42.52, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=74.33, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.13, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.93, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.73, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(36.0)
                Voice('6')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
        with Measure(number='24', width=193.18):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=70.53, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=131.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=40.26, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=70.53, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=100.79, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=131.05, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=161.31, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='25', width=299.01):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(138.05)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=109.18, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=203.3, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=234.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=266.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=109.18, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.55, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=171.92, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.3, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=234.67, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=266.04, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='26', width=187.19):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.26, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=97.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=127.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=156.32, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.26, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.53, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=97.79, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=127.06, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=156.32, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='27', width=204.24):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=30.0)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.26, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.53, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=97.79, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=127.06, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=156.32, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='28', width=157.76):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=30.0)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=133.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=34.63, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=59.25, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.88, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=108.5, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.13, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Barline(location='right'):
                Ending(None, number='2', type='stop')
        with Measure(number='29', width=186.81):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=37.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=86.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=111.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=135.96, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=160.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=37.46, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=62.08, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=86.71, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=111.33, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=135.96, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.59, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='30', width=159.36):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=133.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=34.63, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=59.25, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.88, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=108.5, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.13, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='31', width=275.28):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(138.05)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=109.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=136.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=189.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=219.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=219.84, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=246.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=246.76, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=109.18, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=136.1, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.02, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=189.94, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.84, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=246.76, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='32', width=159.73):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=10.0, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=58.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=58.59, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=133.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=34.29, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=58.59, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=82.88, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=109.55, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.84, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='33', width=183.84):
            with Note(default_x=10.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=111.73, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=127.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=10.72, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.97, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=61.22, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=86.48, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=111.73, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=143.29, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.72, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=61.22, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=111.73, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='34', width=158.02):
            with Note(default_x=16.56, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=86.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=109.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=133.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.35, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=16.56, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.87, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=63.18, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=86.49, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=109.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.11, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=16.2, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(24.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=109.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='35', width=164.1):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=36.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=61.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=87.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=112.17, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=137.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.67, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.35, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=61.83, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=87.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=112.17, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.34, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=61.83, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=112.17, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='36', width=170.34):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=42.85)
            with Note(default_x=16.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=16.2, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=16.2, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=38.66, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=61.13, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.59, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.06, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=128.52, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='37', width=83.06):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=42.85)
            with Note(default_x=16.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=16.2, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=16.2, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D.C. al Fine', relative_x=1.9, relative_y=56.15)
                Sound(dacapo='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='stop')
        with Measure(number='1', width=228.94):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(70.85)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(73.38)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('3')
                    BeatType('4')
                Staves(2)
            with Note(default_x=115.23, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=152.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=189.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(18.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='2', width=161.01):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=10.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=10.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-143.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-108.38):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.04, default_y=-158.38):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=60.04, default_y=-123.38):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=109.73, default_y=-143.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=109.73, default_y=-108.38):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=239.21):
            with Note(default_x=21.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=98.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=126.23, default_y=-20.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=154.42, default_y=-15.0):
                with Pitch():
                    Step('C')
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
            with Note(default_x=182.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=21.87, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=21.87, default_y=-148.38):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=21.87, default_y=-113.38):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=98.04, default_y=-158.38):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=98.04, default_y=-123.38):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=182.61, default_y=-148.38):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=182.61, default_y=-113.38):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=166.85):
            with Note(default_x=15.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.84, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=15.84, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=16.2, default_y=-143.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=16.2, default_y=-108.38):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=65.88, default_y=-158.38):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=65.88, default_y=-123.38):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=115.57, default_y=-143.38):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=115.57, default_y=-108.38):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=183.54):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-47.1, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=46.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=78.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=78.47, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=78.47, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-138.38):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-103.38):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=78.47, default_y=-158.38):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=78.47, default_y=-123.38):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='6', width=164.81):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=63.84, default_y=-123.38):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=113.53, default_y=-128.38):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=230.77):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(136.47)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=90.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=90.38, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=90.38, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=136.64, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=136.64, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=136.64, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=182.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=182.9, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=182.9, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=90.38, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=136.64, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=182.9, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='8', width=150.39):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=56.26, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=56.26, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=56.26, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=102.53, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=102.53, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=56.26, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=102.53, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='9', width=108.58):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=10.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=10.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='10', width=132.35):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=23.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=59.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=95.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(18.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='11', width=171.67):
            with Note(default_x=13.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=65.89, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=65.89, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=65.89, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=117.98, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=117.98, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=117.98, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=228.95):
            with Note(default_x=21.87, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=58.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=94.41, default_y=-5.0):
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=121.26, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=148.11, default_y=-5.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=174.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=21.87, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=21.87, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=82.55, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=94.41, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=94.41, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=163.1, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=174.97, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=174.97, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=171.67):
            with Note(default_x=13.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=65.89, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=65.89, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=65.89, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=117.98, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=117.98, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=117.98, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=340.88):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(136.47)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-30.0):
                        Sfp()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=94.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=135.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=175.88, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=216.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=257.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=298.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=94.18, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=94.18, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=94.18, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=135.03, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=175.88, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=216.73, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=257.58, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=298.43, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='15', width=152.87):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=10.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=10.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.36, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=10.36, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=57.33, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=57.33, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=104.3, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=104.3, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=231.07):
            with Note(default_x=21.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=58.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=95.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=122.29, default_y=-20.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=149.42, default_y=-15.0):
                with Pitch():
                    Step('C')
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
            with Note(default_x=176.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=21.87, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=21.87, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=21.87, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=95.16, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=95.16, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=176.55, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=176.55, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=206.56):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=42.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=74.99, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=74.99, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=107.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.48, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=139.97, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=139.97, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=172.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=172.47, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=74.99, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=74.99, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=139.97, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=139.97, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='18', width=119.98):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=66.19)
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=10.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=66.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=66.2, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=10.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='19', width=143.01):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=66.19)
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=10.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=64.4, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=64.4, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Fine', relative_y=20.0)
                Sound(fine='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='2', type='stop')
        with Measure(number='20', width=165.96):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(136.47)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Trio.', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sfp()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=112.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='21', width=206.39):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=44.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=79.57, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=114.35, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=20.0):
                        Sfp()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=149.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(24.0)
            with Note(default_x=149.14, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=79.57, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=149.14, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=193.28):
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=42.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=74.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=107.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=28.01):
                        Sfp()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=139.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(24.0)
            with Note(default_x=139.77, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=74.89, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=139.77, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=193.28):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=42.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=74.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=107.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=33.76):
                        Sfp()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=139.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(24.0)
            with Note(default_x=139.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=74.89, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=139.77, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='24', width=197.65):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=43.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=109.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-20.0):
                        Sfp()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=142.9, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=142.9, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.45, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='25', width=237.79):
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=53.51, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=53.51, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=93.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.23, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=132.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=132.94, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-30.0):
                        Sfp()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=172.65, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=172.65, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(24.0)
            with Note(default_x=172.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=93.23, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=172.65, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=309.08):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(136.47)
                with StaffLayout(number=2):
                    StaffDistance(70.98)
            with Note(default_x=94.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=94.18, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=236.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=236.38, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=271.93, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=271.93, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=94.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=129.73, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=165.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=200.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=236.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=94.18, default_y=-110.98):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=165.28, default_y=-120.98):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='27', width=269.41):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=56.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=56.14, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=98.47, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=98.47, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=140.81, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=140.81, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=183.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=183.14, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=225.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=225.48, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-105.98):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=98.47, default_y=-100.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=183.14, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='28', width=130.96):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-120.98):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=61.15, default_y=-155.98):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='29', width=80.44):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sfp()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=24.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='30', width=202.52):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=44.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=78.19, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=112.28, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sfp()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=146.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-150.98):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=78.19, default_y=-115.98):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=146.37, default_y=-120.98):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=146.37, default_y=-105.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='31', width=201.95):
            with Note(default_x=13.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.11, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=80.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=113.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=147.05, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=147.05, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-125.98):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-100.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=80.42, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='32', width=257.51):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(136.47)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=90.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=119.94, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=149.5, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=179.06, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-30.0):
                        Sfp()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=208.61, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=90.38, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=149.5, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=208.61, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=208.61, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='33', width=164.02):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=64.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=91.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-20.0):
                        Sfp()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=118.87, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=118.87, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=64.44, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='34', width=202.78):
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=47.26, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=47.26, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=80.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=80.72, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=114.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=114.18, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-20.0):
                        Sfp()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=147.64, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=147.64, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=80.72, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='35', width=229.54):
            with Note(default_x=13.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=49.49, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=49.49, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=85.18, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=85.18, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=120.87, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=120.87, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=156.56, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=156.56, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=192.25, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=192.25, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=85.18, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='36', width=229.54):
            with Note(default_x=13.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=49.49, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=49.49, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=85.18, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.18, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=120.87, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.87, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=156.56, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=156.56, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=192.25, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=192.25, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=85.18, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=156.56, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='37', width=110.98):
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=53.06, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D.C. al Fine', default_y=5.87, relative_y=20.0)
                Sound(dacapo='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='1', width=145.68):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(70.85)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(74.01)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('3')
                    BeatType('4')
                Staves(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=116.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=116.07, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=116.07, default_y=-169.01):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=116.07, default_y=-134.01):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='2', width=184.1):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=58.84, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=78.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.33, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-134.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=58.84, default_y=-139.01):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=78.31, default_y=-134.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.45, default_y=-129.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.6, default_y=-134.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.07, default_y=-139.01):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.33, default_y=-144.01):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='3', width=117.45):
            with Note(default_x=13.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=68.45, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=92.68, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-149.01):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=68.45, default_y=-184.01):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=68.45, default_y=-149.01):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=92.68, default_y=-184.01):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=92.68, default_y=-149.01):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='4', width=166.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=54.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=72.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=89.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.39, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.85, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-154.01):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=10.0, default_y=-119.01):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=54.54, default_y=-124.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=72.01, default_y=-119.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=89.47, default_y=-114.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.93, default_y=-119.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.39, default_y=-124.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.85, default_y=-129.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='5', width=86.4):
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=59.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-134.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='6', width=183.57):
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=76.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=92.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-169.01):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-134.01):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=50.05, default_y=-134.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=50.05, default_y=-99.01):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='7', width=260.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=30.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=50.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=91.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=111.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.52, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-45.32, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=172.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=192.28, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.54, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('5')
                Staff(2)
        with Measure(number='8', width=219.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(135.28)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=95.01, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=127.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=144.32, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=144.32, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=144.32, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=181.08, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=181.08, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=181.08, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=95.01, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=144.32, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=181.08, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='9', width=92.31):
            with Note(default_x=13.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='10', width=59.21):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.59, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='11', width=260.58):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=133.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=153.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=174.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=194.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.53, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.06, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.59, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=92.11, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.64, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.17, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.7, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=174.23, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=194.76, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.28, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.81, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=289.59):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=110.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=154.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=176.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=198.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=220.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.03, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.7, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.59, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.62, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.65, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.68, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.71, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=198.74, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=220.77, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.83, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='13', width=273.23):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=100.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=184.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(36.0)
            with Note(default_x=10.0, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.18, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.85, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.02, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=100.2, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.38, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.56, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.74, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=184.92, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=206.1, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.28, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.46, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=361.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(135.28)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=269.55, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=91.21, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.5, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.09, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.38, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.67, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.97, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.26, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=269.55, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.84, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.14, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.43, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='15', width=259.79):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(18.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=108.56, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=133.5, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=158.44, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=183.38, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.31, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.25, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=68.66, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=68.66, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=68.66, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='16', width=313.26):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.16, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=111.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=135.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.96, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=208.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=233.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note():
                Rest(measure='yes')
                Duration(36.0)
                Voice('5')
                Staff(2)
        with Measure(number='17', width=158.68):
            with Note(default_x=10.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=49.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=69.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=69.61, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=69.61, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=113.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=113.34, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=113.34, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=69.61, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=113.34, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='18', width=101.45):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=10.0, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Fine', relative_y=20.0)
                Sound(fine='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='19', width=219.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(135.28)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Trio.', default_y=1.07, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
            with Note(default_x=142.43, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=192.21, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Attributes():
                with Clef(number=2, after_barline='yes'):
                    Sign('G')
                    Line(2)
            with Note(default_x=142.43, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=192.21, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='20', width=239.83):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Fp()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=88.85, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=88.85, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=163.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=163.54, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.16, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=14.16, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=88.85, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=88.85, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=163.54, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=163.54, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='21', width=239.83):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(36.0)
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
                Duration(36.0)
            with Note(default_x=14.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=14.16, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=88.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=88.85, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=163.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=163.54, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.16, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=14.16, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=88.85, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=88.85, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=163.54, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=163.54, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='22', width=265.91):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=95.64, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=177.47, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Forward():
                Duration(6.0)
            with Note(default_x=107.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=107.5, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Forward():
                Duration(6.0)
            with Note(default_x=177.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=177.47, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(30.0)
            with Note(default_x=13.8, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=95.64, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=95.64, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=95.64, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=177.47, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=177.47, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='23', width=229.46):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=160.1, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=204.7, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=13.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=86.95, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=160.1, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=204.7, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='24', width=241.75):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(135.28)
                with StaffLayout(number=2):
                    StaffDistance(76.28)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Fp()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=95.01, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=143.63, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=143.63, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=191.89, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=191.89, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=95.37, default_y=-106.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=95.37, default_y=-96.28):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=143.63, default_y=-111.28):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=143.63, default_y=-101.28):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=191.89, default_y=-116.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=191.89, default_y=-106.28):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='25', width=168.17):
            with Note(default_x=21.03, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(36.0)
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
                Duration(36.0)
            with Note(default_x=21.39, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=21.39, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=69.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=69.79, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=118.18, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=118.18, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=21.39, default_y=-131.28):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=21.39, default_y=-111.28):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=69.79, default_y=-141.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=69.79, default_y=-116.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=118.18, default_y=-131.28):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=118.18, default_y=-111.28):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='26', width=187.45):
            with Note(default_x=13.8, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=69.47, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=130.18, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Forward():
                Duration(6.0)
            with Note(default_x=81.33, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=81.33, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Forward():
                Duration(6.0)
            with Note(default_x=130.18, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=130.18, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(30.0)
            with Note(default_x=13.8, default_y=-116.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-106.28):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=69.47, default_y=-111.28):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=69.47, default_y=-101.28):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=130.18, default_y=-131.28):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=130.18, default_y=-111.28):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='27', width=137.61):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=13.8, default_y=-116.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=66.38, default_y=-151.28):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='28', width=77.19):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=54.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='29', width=189.57):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=124.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=164.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=26.39, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=26.39, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=59.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=59.24, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=14.16, default_y=-166.28):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=14.16, default_y=-156.28):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=14.16, default_y=-146.28):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=59.24, default_y=-161.28):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=59.24, default_y=-151.28):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='30', width=192.64):
            with Note(default_x=16.87, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=127.89, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=167.87, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=29.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=29.46, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=62.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=62.32, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.23, default_y=-161.28):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=17.23, default_y=-151.28):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=17.23, default_y=-141.28):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=62.32, default_y=-156.28):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=62.32, default_y=-146.28):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=127.89, default_y=-146.28):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=167.87, default_y=-136.28):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='31', width=244.96):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(135.28)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=102.24, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=196.44, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=114.83, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=114.83, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=149.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=149.52, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=196.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=102.6, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=102.6, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=102.6, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=149.52, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=149.52, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=196.44, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='32', width=234.16):
            with Note(default_x=13.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=68.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=158.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=207.56, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=68.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(18.0)
            with Note(default_x=13.8, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=68.8, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=158.79, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=207.56, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='33', width=174.12):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Fp()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(36.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(36.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=66.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=66.95, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=119.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=119.73, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.16, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=14.16, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=66.95, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=66.95, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=119.73, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=119.73, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='34', width=202.79):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(36.0)
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
                Duration(36.0)
            with Note(default_x=14.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=14.16, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=76.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=76.5, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=138.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=138.84, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.16, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=14.16, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=76.5, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=76.5, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=138.84, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=138.84, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='35', width=195.62):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=73.87, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=133.95, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Forward():
                Duration(6.0)
            with Note(default_x=85.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=85.74, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Forward():
                Duration(6.0)
            with Note(default_x=133.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=133.95, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(30.0)
            with Note(default_x=13.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=73.87, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=73.87, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=133.95, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=133.95, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='36', width=142.72):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(12.0)
            with Note(default_x=10.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=67.03, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D.C. al Fine', relative_y=20.0)
                Sound(dacapo='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='1', width=155.71):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(70.85)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                Staves(2)
            with Note(default_x=83.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=130.14, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='2', width=195.11):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=138.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=138.33, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=138.33, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.16, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=14.16, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=83.14, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=83.14, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=138.33, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=138.33, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='3', width=160.18):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=62.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=62.06, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=110.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=110.32, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=62.06, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=62.06, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=62.06, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=110.32, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=110.32, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=110.32, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='4', width=245.35):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=74.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=74.03, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=134.25, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=161.63, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.0, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.38, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=74.03, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=74.03, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=85.89, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=134.25, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=134.25, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=134.25, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='5', width=171.64):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=103.66, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=143.5, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=58.73, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='6', width=216.38):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=152.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=152.51, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=14.16, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=14.16, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=90.23, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=90.23, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=90.23, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=152.51, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=152.51, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=164.37, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=152.51, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='7', width=250.55):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(128.07)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=63.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=63.6, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=125.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=125.38, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=187.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=187.17, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=63.6, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=63.6, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=63.6, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=63.6, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=125.38, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=125.38, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=137.25, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=125.38, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=187.17, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=187.17, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=187.17, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='8', width=223.18):
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=81.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=81.39, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=148.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=148.99, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=81.39, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=148.99, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=148.99, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.44, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(12.0)
        with Measure(number='9', width=134.18):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=10.0, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=62.76, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='10', width=106.29):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.59, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=77.55, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='11', width=251.01):
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=92.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=92.34, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=131.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=131.6, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=170.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=170.87, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=210.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=210.14, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=13.8, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=53.07, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.34, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.34, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=131.6, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=170.87, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=170.87, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=210.14, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='12', width=229.16):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=85.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=85.05, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=156.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=156.31, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=191.93, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=13.8, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=49.43, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=85.05, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=85.05, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=120.68, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=156.31, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=156.31, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=191.93, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='13', width=277.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(128.07)
                with StaffLayout(number=2):
                    StaffDistance(66.62)
            with Note(default_x=61.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=97.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=132.73, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=132.73, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=168.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=168.41, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=204.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=204.09, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=239.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=239.77, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=61.37, default_y=-101.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=61.37, default_y=-91.62):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=97.05, default_y=-111.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=132.73, default_y=-101.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=132.73, default_y=-91.62):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=168.41, default_y=-111.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=204.09, default_y=-101.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=204.09, default_y=-91.62):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=239.77, default_y=-111.62):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='14', width=278.82):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=98.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=98.1, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=182.39, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=250.88, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-91.62):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=-81.62):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=55.95, default_y=-96.62):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=55.95, default_y=-86.62):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=98.1, default_y=-91.62):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.1, default_y=-81.62):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=140.24, default_y=-96.62):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=140.24, default_y=-86.62):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=182.39, default_y=-91.62):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.39, default_y=-81.62):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=224.54, default_y=-101.62):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=224.54, default_y=-91.62):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=170.7):
            with Note(default_x=17.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=17.44, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=17.44, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=118.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=118.66, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=118.66, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=17.8, default_y=-131.62):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=17.8, default_y=-96.62):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=68.23, default_y=-131.62):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=68.23, default_y=-96.62):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=118.66, default_y=-131.62):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=118.66, default_y=-96.62):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=174.32):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=66.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=66.77, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=66.77, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=119.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=119.75, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=119.75, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-131.62):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-96.62):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=66.77, default_y=-146.62):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=66.77, default_y=-111.62):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=119.75, default_y=-141.62):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=119.75, default_y=-106.62):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=166.7):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=64.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=64.23, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=64.23, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=114.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=114.66, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=114.66, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-151.62):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-116.62):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=64.23, default_y=-161.62):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=64.23, default_y=-126.62):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=114.66, default_y=-146.62):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=114.66, default_y=-111.62):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='18', width=126.78):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-166.62):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-131.62):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=60.96, default_y=-131.62):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.96, default_y=-96.62):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Fine', relative_y=20.0)
                Sound(fine='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='19', width=161.12):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(-0.0)
                    SystemDistance(128.07)
                with StaffLayout(number=2):
                    StaffDistance(82.94)
            with Attributes():
                with Time():
                    Beats('3')
                    BeatType('4')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Trio', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-54.55, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=86.23, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=134.68, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(12.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=86.23, default_y=-162.94):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=134.68, default_y=-162.94):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='20', width=186.31):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=64.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=64.95, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=116.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=116.1, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=161.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=161.46, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-147.94):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=64.95, default_y=-137.94):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=64.95, default_y=-112.94):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=116.1, default_y=-137.94):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=116.1, default_y=-112.94):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=161.46, default_y=-137.94):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=161.46, default_y=-112.94):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='21', width=214.02):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=66.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=66.13, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=142.23, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=188.64, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-127.94):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=-107.94):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=66.13, default_y=-137.94):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=66.13, default_y=-112.94):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=142.23, default_y=-162.94):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=188.64, default_y=-162.94):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='22', width=186.31):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=64.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=64.95, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=116.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=116.1, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=161.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=161.46, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-147.94):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=64.95, default_y=-112.94):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=64.95, default_y=-102.94):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=116.1, default_y=-112.94):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=116.1, default_y=-102.94):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=161.46, default_y=-112.94):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=161.46, default_y=-102.94):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='23', width=253.69):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=72.94, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.94, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-127.94):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=-107.94):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.94, default_y=-112.94):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.94, default_y=-102.94):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=172.76, default_y=-172.94):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=172.76, default_y=-137.94):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=225.21, default_y=-172.94):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=225.21, default_y=-137.94):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='24', width=192.91):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=66.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=66.93, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=66.93, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=120.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=120.05, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=120.05, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-182.94):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-147.94):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=120.05, default_y=-192.94):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=120.05, default_y=-157.94):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=167.17, default_y=-192.94):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=167.17, default_y=-157.94):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='25', width=292.18):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(-0.0)
                    SystemDistance(128.07)
                with StaffLayout(number=2):
                    StaffDistance(77.52)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=123.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.8, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=123.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=209.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=209.83, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=63.6, default_y=-182.52):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=63.6, default_y=-147.52):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=209.83, default_y=-142.52):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=209.83, default_y=-107.52):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=263.21, default_y=-142.52):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=263.21, default_y=-107.52):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='26', width=219.55):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=74.9, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=74.9, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=74.9, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=135.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=124.13, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=135.99, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=135.99, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-137.52):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-102.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=135.99, default_y=-137.52):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=135.99, default_y=-102.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=190.17, default_y=-137.52):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=190.17, default_y=-102.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='27', width=127.82):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=10.0, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=10.0, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=10.0, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-157.52):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=10.0, default_y=-122.52):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='28', width=102.17):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-54.55, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=23.66, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=74.51, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=23.66, default_y=-157.52):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=74.51, default_y=-157.52):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='29', width=231.1):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-62.62, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=20.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=75.19, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=155.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=155.47, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=204.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=204.42, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=20.0, default_y=-152.52):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=75.19, default_y=-157.52):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=155.47, default_y=-122.52):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=155.47, default_y=-102.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=204.42, default_y=-122.52):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=204.42, default_y=-102.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='30', width=221.55):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=20.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=20.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=72.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.67, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=149.29, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=196.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=20.0, default_y=-117.52):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=20.0, default_y=-107.52):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.67, default_y=-122.52):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=72.67, default_y=-102.52):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=149.29, default_y=-157.52):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=196.0, default_y=-157.52):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='31', width=261.85):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(128.07)
                with StaffLayout(number=2):
                    StaffDistance(89.26)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-69.95, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=73.41, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=122.4, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=193.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=193.65, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=237.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=237.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=73.41, default_y=-174.26):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=122.4, default_y=-169.26):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=193.65, default_y=-134.26):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=193.65, default_y=-114.26):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=237.09, default_y=-134.26):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=237.09, default_y=-114.26):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='32', width=238.55):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=20.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=20.0, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=73.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=73.52, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=20.0, default_y=-139.26):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=20.0, default_y=-109.26):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=73.52, default_y=-134.26):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=73.52, default_y=-114.26):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=165.17, default_y=-194.26):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=165.17, default_y=-159.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=212.63, default_y=-194.26):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=212.63, default_y=-159.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='33', width=175.61):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=61.27, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=61.27, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=61.27, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=108.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=108.75, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=108.75, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-179.26):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-144.26):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=108.75, default_y=-189.26):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=108.75, default_y=-154.26):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=150.85, default_y=-189.26):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=150.85, default_y=-154.26):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='34', width=188.5):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=65.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=65.61, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=65.61, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=117.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=117.41, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=117.41, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=117.41, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-199.26):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-164.26):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=117.41, default_y=-199.26):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=117.41, default_y=-164.26):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=163.35, default_y=-199.26):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=163.35, default_y=-164.26):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='35', width=213.33):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=70.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=70.04, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=70.04, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=70.04, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=136.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=124.42, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=136.29, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=136.29, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-194.26):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-159.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=136.29, default_y=-169.26):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=136.29, default_y=-134.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(9.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=186.17, default_y=-169.26):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=186.17, default_y=-134.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='36', width=116.51):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-189.26):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-154.26):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('D.C. al Fine', default_y=10.87, relative_y=20.0)
                Sound(dacapo='yes')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')