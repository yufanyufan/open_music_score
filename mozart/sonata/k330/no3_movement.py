with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Piano Sonata No. 10 in C major')
    with Identification():
        Creator('Wolfgang Amadeus Mozart 1756–91', type='composer')
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
        CreditWords('Piano Sonata No. 10 in C major - 3rd Movement', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Wolfgang Amadeus Mozart 1756–91', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
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
        with Measure(number='1', width=206.02):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(24.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('2')
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
                    with Metronome(parentheses='no', default_x=-36.12, default_y=23.09, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                with DirectionType():
                    Words('\n', default_x=-36.12, default_y=23.09, relative_y=20.0, font_weight='bold', font_size='12')
                    Words(None)
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=82.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=124.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=140.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=155.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=180.13, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=106.84, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=155.84, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=180.13, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='2', width=120.04):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=53.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=69.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=38.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=69.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.24, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=69.57, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=94.01, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='3', width=133.6):
            with Note(default_x=10.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.08, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=67.74, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=83.41, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=107.7, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=34.41, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=83.41, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=107.7, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='4', width=102.81):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=35.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=35.22, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=56.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=56.63, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.22, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=56.63, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=78.05, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='5', width=133.48):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.96, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=67.63, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=83.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=107.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=34.29, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.29, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=107.58, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='6', width=149.82):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=56.29, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=79.55, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=99.02, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=123.62, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.4, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=99.02, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=123.62, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='7', width=210.73):
            with Note(default_x=43.32, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.11, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=80.9, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=99.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=118.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=137.27, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=156.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=185.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=80.9, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=80.9, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=156.06, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=156.06, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='8', width=259.1):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(121.51)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=72.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=94.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=166.68, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=189.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=234.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=72.35, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.35, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='9', width=214.04):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=101.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=116.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=164.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=164.64, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.7, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=61.6, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.51, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=116.84, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.74, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.64, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.54, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='10', width=184.65):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=52.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=74.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=95.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=52.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=95.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.41, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.82, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.24, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=95.65, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.06, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.47, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.89, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=214.04):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=101.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=116.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=164.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=164.64, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.7, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=61.6, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.51, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=116.84, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.74, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.64, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.54, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=184.65):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=10.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=52.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=52.82, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=95.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=95.65, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.41, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.82, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.24, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=95.65, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.06, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.47, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.89, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='13', width=287.45):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(121.51)
                with StaffLayout(number=2):
                    StaffDistance(80.79)
            with Note(default_x=61.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=143.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=160.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=177.01, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=231.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=61.37, default_y=-120.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=88.58, default_y=-110.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.79, default_y=-120.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.0, default_y=-110.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=177.01, default_y=-125.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=204.22, default_y=-110.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.43, default_y=-125.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.64, default_y=-110.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=252.42):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=97.07, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=120.33, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=139.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=195.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-130.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.56, default_y=-110.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.31, default_y=-130.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.07, default_y=-110.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=139.8, default_y=-135.79):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=167.55, default_y=-110.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.31, default_y=-135.79):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.06, default_y=-110.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='15', width=204.15):
            with Note(default_x=17.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.97, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=161.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=68.71, default_y=-130.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=120.19, default_y=-125.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=68.71, default_y=-105.79):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=120.19, default_y=-100.79):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=161.37, default_y=-105.79):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='16', width=312.47):
            with Note(default_x=13.8, default_y=-15.0):
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
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=38.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=63.31, default_y=-5.0):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='stop')
            with Note(default_x=88.07, default_y=-15.0):
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=112.82, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=137.58, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=162.34, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
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
            with Note(default_x=187.09, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=211.85, default_y=10.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='stop')
            with Note(default_x=236.61, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=261.36, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.12, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Backup():
                Duration(48.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('legato', relative_x=37.33, relative_y=9.0, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=13.8, default_y=-110.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-100.79):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='17', width=339.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(121.51)
                with StaffLayout(number=2):
                    StaffDistance(111.44)
            with Note(default_x=72.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=93.92, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=115.49, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=137.06, default_y=10.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=158.63, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.2, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=201.77, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=223.34, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=250.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=271.58, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=293.15, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=314.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=137.06, default_y=-161.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=137.06, default_y=-151.44):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=137.06, default_y=-136.44):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=201.77, default_y=-156.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=201.77, default_y=-141.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=201.77, default_y=-131.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=271.58, default_y=-136.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=271.58, default_y=-126.44):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='18', width=289.74):
            with Note(default_x=13.8, default_y=-15.0):
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
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=36.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=59.28, default_y=-5.0):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='stop')
            with Note(default_x=82.01, default_y=-15.0):
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=104.75, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=127.49, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=150.23, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
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
            with Note(default_x=173.49, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=196.76, default_y=10.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='stop')
            with Note(default_x=219.5, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=242.23, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.97, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-141.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-131.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='19', width=284.37):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=38.8, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=60.37, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=81.94, default_y=10.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=103.51, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.08, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=146.65, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=168.22, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=194.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=216.46, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=238.03, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=259.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=81.94, default_y=-161.44):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=81.94, default_y=-151.44):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=81.94, default_y=-136.44):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=146.65, default_y=-156.44):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=146.65, default_y=-141.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=146.65, default_y=-131.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=216.46, default_y=-136.44):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=216.46, default_y=-126.44):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='20', width=142.9):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=81.86, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-141.44):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=13.8, default_y=-131.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=47.83, default_y=-156.44):
                with Pitch():
                    Step('G')
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
            with Note(default_x=81.86, default_y=-211.44):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=81.86, default_y=-176.44):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='21', width=245.07):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(121.51)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=63.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=154.56, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=165.52, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=176.49, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=187.45, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=199.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=220.31, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('legato', default_y=-40.0, relative_x=5.33, relative_y=-39.0, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=63.6, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=84.73, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.63, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.77, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=156.9, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=178.04, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.17, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.31, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='22', width=207.75):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=104.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=160.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.52, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.19, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.71, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=104.24, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.76, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.46, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=182.99, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='23', width=179.62):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=54.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=94.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=134.7, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=154.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.95, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.1, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.25, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=94.4, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=114.55, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.7, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.85, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=224.6):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=89.22, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=104.89, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=131.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.56, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.46, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.22, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=131.55, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=154.31, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.08, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.84, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='25', width=199.45):
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=108.24, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=119.21, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=130.17, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=141.14, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=152.85, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=174.69, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.63, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.53, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.36, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.19, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=131.02, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.85, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.69, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='26', width=264.62):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=59.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.02, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=162.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=187.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=212.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=237.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=59.8, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.02, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.25, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.47, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=162.13, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=187.36, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.58, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='27', width=252.5):
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=43.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=73.08, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=102.71, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=132.35, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=161.99, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=191.63, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=221.27, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=43.44, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.08, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.71, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=132.35, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=161.99, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.63, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.27, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='28', width=213.75):
            with Note(default_x=21.03, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=116.59, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=21.03, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.92, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.81, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.7, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=116.59, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.48, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.37, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.26, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='29', width=325.61):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=91.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=117.2, default_y=10.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=143.06, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
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
            with Note(default_x=168.91, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
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
            with Note(default_x=194.76, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
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
            with Note(default_x=220.61, default_y=10.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='stop')
            with Note(default_x=246.46, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=272.31, default_y=10.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=298.16, default_y=-5.0):
                with Pitch():
                    Step('E')
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
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
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=39.65, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.5, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=91.35, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='30', width=320.85):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(98.69)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=63.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=125.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=146.25, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=166.91, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=190.17, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
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
            with Note(default_x=213.44, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=234.1, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='stop')
            with Note(default_x=254.76, default_y=15.0):
                with Pitch():
                    Step('B')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=275.42, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=296.08, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=63.6, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=84.26, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.92, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=125.58, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='31', width=302.68):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=76.19, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=95.57, default_y=10.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='stop')
            with Note(default_x=118.83, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=142.1, default_y=10.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=161.48, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=200.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=219.61, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='stop')
            with Note(default_x=239.08, default_y=15.0):
                with Pitch():
                    Step('B')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=258.54, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=277.92, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=56.81, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=56.81, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=56.81, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=180.85, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=180.85, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=180.85, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='32', width=228.04):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.08, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=73.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.36, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.06, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=98.62, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.18, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=149.75, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.31, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.88, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='33', width=204.92):
            with Note(default_x=11.75, default_y=-30.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=30.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=110.24, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=140.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=30.2, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=50.21, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.22, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.23, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.24, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.14, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.14, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.15, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='34', width=230.57):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(98.69)
                with StaffLayout(number=2):
                    StaffDistance(67.83)
            with Note(default_x=61.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=80.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=118.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=148.54, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=186.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=61.37, default_y=-107.83):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=80.46, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.55, default_y=-112.83):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=118.64, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=148.54, default_y=-117.83):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=167.63, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.72, default_y=-127.83):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.8, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='35', width=234.18):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=78.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('legato', default_y=-40.0, relative_x=-4.0, relative_y=-24.33, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=17.23, default_y=-112.83):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=42.95, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.26, default_y=-97.83):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.98, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=129.7, default_y=-97.83):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.42, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.14, default_y=-87.83):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.86, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='36', width=204.78):
            with Note():
                Rest(measure='yes')
                Duration(48.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=17.8, default_y=-97.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.07, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.17, default_y=-102.83):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.28, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.54, default_y=-97.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=133.81, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.91, default_y=-107.83):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.02, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='37', width=207.76):
            with Note(default_x=11.75, default_y=-30.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=30.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=112.13, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=142.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=183.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=30.2, default_y=-102.83):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=50.69, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.17, default_y=-112.83):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.65, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.13, default_y=-102.83):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.03, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.51, default_y=-112.83):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=183.0, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='38', width=179.2):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=29.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.16, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=135.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-107.83):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.09, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.18, default_y=-112.83):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.27, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.16, default_y=-117.83):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.25, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.34, default_y=-127.83):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.43, default_y=-92.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=295.23):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(98.69)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=173.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=219.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=237.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=265.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=61.37, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=89.51, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=117.65, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.78, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=173.92, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.06, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.36, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.49, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=259.81):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=128.01, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=175.94, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=199.21, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=228.71, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.5, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=98.5, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=128.01, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=157.51, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.21, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.71, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='41', width=243.15):
            with Note(default_x=13.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=121.07, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=164.65, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=187.92, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=214.74, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.62, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.44, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.25, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.07, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=147.89, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.92, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.74, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='42', width=258.3):
            with Note(default_x=13.8, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.16, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=74.52, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=104.89, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=135.25, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=195.97, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.16, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.52, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.89, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.25, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=165.61, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.97, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.33, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='43', width=294.15):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(98.69)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=64.11, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=119.38, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=174.65, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=220.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=237.28, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=264.91, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=64.11, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=91.75, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.38, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.02, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=174.65, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.29, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.28, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.91, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='44', width=255.99):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=126.0, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=173.13, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=196.39, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=225.39, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.0, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.0, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=126.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.0, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.39, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.39, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='45', width=239.33):
            with Note(default_x=13.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=119.07, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=161.83, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=185.1, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=211.42, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.12, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.43, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.75, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.07, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.39, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.1, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.42, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='46', width=267.02):
            with Note(default_x=13.8, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.25, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=76.7, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.16, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=139.61, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=171.06, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=202.51, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.96, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=45.25, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.7, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.16, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=139.61, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=171.06, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.51, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=233.96, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='47', width=294.75):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(98.69)
                with StaffLayout(number=2):
                    StaffDistance(72.01)
            with Note(default_x=64.11, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=101.41, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=124.68, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=144.14, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=174.04, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=193.16, default_y=10.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=212.28, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Tuplet(type='stop')
            with Note(default_x=231.4, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=250.87, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=269.99, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=101.41, default_y=-117.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=101.41, default_y=-107.01):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=174.04, default_y=-112.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=174.04, default_y=-102.01):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=231.4, default_y=-107.01):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=231.4, default_y=-97.01):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='48', width=258.65):
            with Note(default_x=13.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=50.85, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=82.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.35, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=131.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=150.24, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=169.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
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
                    Tuplet(type='stop')
            with Note(default_x=195.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=214.89, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=233.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=50.85, default_y=-132.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=50.85, default_y=-122.01):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=131.25, default_y=-127.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=131.25, default_y=-117.01):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=195.9, default_y=-122.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=195.9, default_y=-112.01):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='49', width=244.44):
            with Note(default_x=13.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.1, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=74.37, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=93.83, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=123.73, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=142.85, default_y=10.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=161.97, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Tuplet(type='stop')
            with Note(default_x=181.09, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=200.56, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=219.68, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=51.1, default_y=-117.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.1, default_y=-107.01):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=123.73, default_y=-112.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=123.73, default_y=-102.01):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=181.09, default_y=-107.01):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=181.09, default_y=-97.01):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='50', width=258.65):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=50.85, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=82.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.35, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=131.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=150.24, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=169.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
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
                    Tuplet(type='stop')
            with Note(default_x=195.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=214.89, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=233.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=50.85, default_y=-132.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=50.85, default_y=-122.01):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=131.25, default_y=-127.01):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=131.25, default_y=-117.01):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=195.9, default_y=-122.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=195.9, default_y=-112.01):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='51', width=327.85):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(67.26)
            with Note(default_x=61.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=105.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
                    Tuplet(type='stop')
            with Note(default_x=127.29, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=149.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Note(default_x=171.24, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=193.22, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=215.19, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=237.17, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='stop')
            with Note(default_x=259.14, default_y=15.0):
                with Pitch():
                    Step('B')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=281.11, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=303.09, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Backup():
                Duration(48.0)
            with Note(default_x=61.37, default_y=-112.26):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='52', width=325.82):
            with Note(default_x=13.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
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
            with Note(default_x=39.6, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=65.39, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
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
                    Tuplet(type='stop')
            with Note(default_x=91.19, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=116.98, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
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
            with Note(default_x=142.78, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=168.58, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=194.37, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.17, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Tuplet(type='stop')
            with Note(default_x=245.96, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=271.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=298.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
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
                Duration(48.0)
            with Note(default_x=13.44, default_y=-147.26):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=13.44, default_y=-137.26):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=13.44, default_y=-127.26):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=13.44, default_y=-112.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='53', width=210.67):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=34.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.57, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-132.26):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-112.26):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='54', width=192.15):
            with Note(default_x=10.12, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=137.48, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.48, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=164.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=52.57, default_y=-132.26):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=95.03, default_y=-127.26):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=52.57, default_y=-102.26):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=95.03, default_y=-102.26):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=137.48, default_y=-97.26):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='55', width=316.58):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.2)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=-20.0):
                with Pitch():
                    Step('B')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=82.32, default_y=-30.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=103.27, default_y=-20.0):
                with Pitch():
                    Step('B')
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
                    Tuplet(type='stop')
            with Note(default_x=124.22, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=145.17, default_y=-20.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=166.12, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=187.07, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=208.02, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=228.96, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='stop')
            with Note(default_x=249.91, default_y=15.0):
                with Pitch():
                    Step('B')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=270.86, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=291.81, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Backup():
                Duration(48.0)
            with Note(default_x=61.37, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=61.37, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='56', width=333.9):
            with Note(default_x=13.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
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
            with Note(default_x=39.52, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=65.25, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
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
                    Tuplet(type='stop')
            with Note(default_x=97.31, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=123.03, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
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
            with Note(default_x=148.76, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=177.02, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
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
            with Note(default_x=202.75, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=228.47, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Tuplet(type='stop')
            with Note(default_x=254.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=279.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=306.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
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
                Duration(48.0)
            with Note(default_x=13.44, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=13.44, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=13.44, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=13.44, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(48.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='57', width=199.39):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=32.45, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.35, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=84.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=129.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=174.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='58', width=206.62):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=39.69, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=69.58, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.04, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.49, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.95, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.4, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.86, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=17.23, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=17.23, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='59', width=228.0):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.2)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=88.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=126.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=145.64, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=164.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=184.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('legato', default_y=-40.0, relative_x=-1.33, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=61.37, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=88.04, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.24, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.44, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=145.64, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=164.84, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.04, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.24, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='60', width=196.36):
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=85.7, default_y=-25.0):
                with Pitch():
                    Step('A')
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
                    with Ornaments():
                        TrillMark()
            with Note(default_x=153.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=177.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=28.92, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=47.85, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.77, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=85.7, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=104.62, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.52, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.44, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='61', width=210.64):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=103.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=151.76, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=170.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=185.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.07, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.72, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.37, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.64, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.91, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.56, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.21, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='62', width=210.84):
            with Note(default_x=13.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=68.72, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=115.56, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=162.4, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.22, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.72, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.14, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=115.56, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.98, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.4, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.82, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='63', width=210.64):
            with Note(default_x=13.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=103.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=151.76, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=170.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=185.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.07, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.72, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.37, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.64, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.91, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.56, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.21, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='64', width=265.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(100.2)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=63.6, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=119.19, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=167.37, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=215.55, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=63.6, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=87.69, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.19, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.28, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=167.37, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=191.46, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.55, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.64, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='65', width=266.71):
            with Note(default_x=13.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=95.42, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=113.87, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=195.41, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='stop', number=1)
            with Note(default_x=218.68, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
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
            with Note(default_x=241.94, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
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
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.82, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.84, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.85, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=113.87, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.89, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.39, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.41, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='66', width=266.71):
            with Note(default_x=13.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=95.42, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
            with Note(default_x=113.87, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=195.41, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='stop', number=1)
            with Note(default_x=218.68, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
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
            with Note(default_x=241.94, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
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
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.82, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.84, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.85, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=113.87, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.89, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.39, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.41, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='67', width=127.63):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=35.5, default_y=-45.0):
                with Pitch():
                    Step('D')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=81.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=102.86, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=102.86, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=102.86, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='68', width=130.13):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=13.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=62.78, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=62.78, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.29, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=62.78, default_y=-145.0):
                with Pitch():
                    Step('G')
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
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='69', width=200.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.2)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=84.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=107.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=130.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=153.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Ornaments():
                        TrillMark()
            with Note(default_x=168.55, default_y=-25.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=179.51, default_y=-20.0):
                Grace()
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=84.74, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=107.55, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=130.37, default_y=-110.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=153.63, default_y=-110.0):
                with Pitch():
                    Step('G')
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
            with Backup():
                Duration(48.0)
            with Note(default_x=84.74, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=130.37, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=153.63, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='70', width=114.21):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=80.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=37.19, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=80.45, default_y=-115.0):
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
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=80.45, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='71', width=136.59):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=36.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=71.96, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=95.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=36.94, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=71.96, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=95.1, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=71.96, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='72', width=125.78):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=71.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=34.7, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=71.26, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(36.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Staff(2)
        with Measure(number='73', width=133.82):
            with Note(default_x=10.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=34.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=57.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=87.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=102.04, default_y=-30.0):
                Grace()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.01, default_y=-30.0):
                Grace()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=57.23, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=57.23, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='74', width=94.27):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=31.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=63.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=10.0, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=63.56, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=63.56, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='75', width=158.37):
            with Note(default_x=10.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=42.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=82.07, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=113.79, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.72, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=82.07, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(48.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='76', width=93.13):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=44.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=44.27, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=44.27, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='77', width=255.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(100.2)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=107.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=154.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=207.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Ornaments():
                        TrillMark()
            with Note(default_x=223.27, default_y=-25.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=234.24, default_y=-20.0):
                Grace()
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('legato', default_y=-40.0, relative_x=-1.33, relative_y=-31.0, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=61.37, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=84.54, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.71, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.88, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=154.05, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.22, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.11, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.28, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='78', width=200.66):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=55.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=107.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.67, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.33, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.0, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.9, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.56, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.23, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.9, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='79', width=223.17):
            with Note(default_x=47.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=90.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=133.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=176.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=47.0, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=68.63, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.26, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.89, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=133.52, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.14, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.77, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.4, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='80', width=187.64):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=98.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.1, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.39, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.69, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=98.99, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=120.29, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.58, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.88, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='81', width=189.97):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=100.32, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=143.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.43, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.06, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.69, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=100.32, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.94, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.57, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.2, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='82', width=245.96):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=68.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=155.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=68.6, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=90.4, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.2, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=155.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.59, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.39, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.19, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='83', width=192.32):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=101.66, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=145.59, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.76, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.73, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.69, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.66, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.62, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.59, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.55, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='84', width=203.01):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=109.07, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.06, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.96, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.01, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.07, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.13, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.19, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.25, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='85', width=224.04):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=92.84, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=108.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=124.17, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=173.31, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.37, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.27, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.84, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.17, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=148.74, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.31, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.88, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='86', width=191.16):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=144.59, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.6, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.4, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.2, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.0, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=122.79, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.59, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.39, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='87', width=246.88):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(90.56)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=63.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=106.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=200.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=63.6, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.21, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.82, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.43, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=150.03, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=171.64, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.51, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=222.12, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='88', width=182.56):
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=54.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=137.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.37, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.94, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.51, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=96.08, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=116.66, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.23, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='89', width=211.6):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=59.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=88.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=163.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=186.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.86, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.92, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.79, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=111.85, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.91, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.78, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.84, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='90', width=198.22):
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.05, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=121.93, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=151.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.45, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.43, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.05, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.68, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=100.3, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.93, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.83, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.45, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='91', width=217.23):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=45.7, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=68.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=146.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=169.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=20.0, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=45.7, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.75, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.85, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.36, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.41, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.46, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='92', width=200.77):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(90.56)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=63.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=92.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=128.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=157.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=63.6, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=63.6, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=128.86, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=128.86, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
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
        with Measure(number='93', width=106.07):
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='94', width=148.64):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=42.21, default_y=0.0):
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
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=77.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=106.12, default_y=0.0):
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
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
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
            with Note(default_x=77.72, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=77.72, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=77.72, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=77.72, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
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
        with Measure(number='95', width=104.91):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.29, default_y=0.0):
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
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
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
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='96', width=161.19):
            with Note(default_x=44.89, default_y=-5.0):
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.02, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=98.68, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=114.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=136.42, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=66.97, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=114.35, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=136.42, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='97', width=112.87):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=35.29, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=50.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=66.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=66.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.29, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=66.62, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=88.1, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='98', width=126.42):
            with Note(default_x=10.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.25, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=63.91, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=79.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=101.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.65, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=32.19, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=79.58, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=101.65, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='99', width=95.64):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=32.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=32.82, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=51.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=51.85, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=32.82, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=51.85, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=70.87, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='100', width=179.31):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(90.56)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=100.54, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=116.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=131.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=154.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=61.37, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=84.05, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=131.87, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=154.55, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='101', width=169.26):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=54.84, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=78.1, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=97.57, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=121.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=37.56, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=97.57, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=121.33, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='102', width=171.99):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=10.12, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=28.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=46.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=64.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=82.11, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=100.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=118.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=147.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=46.12, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=46.12, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=118.11, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=118.11, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='103', width=181.74):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=36.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=100.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=119.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=17.23, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=17.23, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='104', width=191.8):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=76.52, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=92.18, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=107.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=147.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=147.3, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.07, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.79, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.52, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.85, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.58, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.3, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.03, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='105', width=162.4):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=46.47, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=64.7, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=82.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=46.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=82.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=28.23, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=46.47, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.7, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=82.94, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.17, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.4, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.64, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='106', width=265.65):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(90.56)
                with StaffLayout(number=2):
                    StaffDistance(69.55)
            with Note(default_x=61.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=134.81, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=150.47, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=166.14, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=215.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=215.09, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=61.37, default_y=-169.55):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.85, default_y=-159.55):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=110.33, default_y=-149.55):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.81, default_y=-134.55):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=166.14, default_y=-159.55):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=190.61, default_y=-124.55):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.09, default_y=-149.55):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.57, default_y=-114.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='107', width=188.68):
            with Note(default_x=10.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=10.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=53.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=53.98, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=97.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=97.95, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-134.55):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.99, default_y=-124.55):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.98, default_y=-114.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.96, default_y=-99.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.95, default_y=-149.55):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=119.94, default_y=-139.55):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.93, default_y=-129.55):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.92, default_y=-114.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='108', width=205.92):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=79.85, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=95.52, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=111.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=157.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-109.55):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=33.28, default_y=-99.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.57, default_y=-109.55):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.85, default_y=-99.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=111.18, default_y=-114.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=134.47, default_y=-99.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.75, default_y=-114.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.03, default_y=-99.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='109', width=222.26):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=84.14, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=107.4, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=126.87, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=173.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-119.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.25, default_y=-99.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.69, default_y=-119.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=84.14, default_y=-99.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=126.87, default_y=-124.55):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=150.32, default_y=-99.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.76, default_y=-124.55):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.21, default_y=-99.55):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='110', width=173.99):
            with Note(default_x=17.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.78, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.33, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=60.33, default_y=-119.55):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=60.33, default_y=-94.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=103.43, default_y=-114.55):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=103.43, default_y=-89.55):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=137.91, default_y=-94.55):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='111', width=302.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(90.56)
                with StaffLayout(number=2):
                    StaffDistance(110.92)
            with Direction(placement='below'):
                with DirectionType():
                    Words('legato', default_y=-40.0, relative_x=36.0, relative_y=-65.67, font_style='italic', font_size='11')
                Staff(1)
            with Note(default_x=61.37, default_y=-15.0):
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
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=80.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=98.96, default_y=-5.0):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='stop')
            with Note(default_x=117.75, default_y=-15.0):
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=136.55, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=155.34, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=174.14, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
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
            with Note(default_x=197.4, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=220.67, default_y=10.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='stop')
            with Note(default_x=240.13, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=258.93, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.72, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Backup():
                Duration(48.0)
            with Note(default_x=61.37, default_y=-140.92):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=61.37, default_y=-130.92):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='112', width=249.55):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=35.32, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=53.41, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.5, default_y=10.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=89.58, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.67, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=125.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=143.85, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=170.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=188.6, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=206.69, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=224.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=71.5, default_y=-160.92):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=71.5, default_y=-150.92):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=71.5, default_y=-135.92):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=125.76, default_y=-155.92):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=125.76, default_y=-140.92):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=125.76, default_y=-130.92):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=188.6, default_y=-135.92):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=188.6, default_y=-125.92):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='113', width=254.91):
            with Note(default_x=13.8, default_y=-15.0):
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
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=32.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=51.39, default_y=-5.0):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='stop')
            with Note(default_x=70.18, default_y=-15.0):
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=88.98, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=107.77, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=126.56, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
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
            with Note(default_x=149.83, default_y=15.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=173.1, default_y=10.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='stop')
            with Note(default_x=192.56, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=211.36, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.15, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-140.92):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-130.92):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='114', width=249.55):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=35.32, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=53.41, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=71.5, default_y=10.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=89.58, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.67, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=125.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=143.85, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=170.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=188.6, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=206.69, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=224.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=71.5, default_y=-160.92):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=71.5, default_y=-150.92):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=71.5, default_y=-135.92):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=125.76, default_y=-155.92):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(24.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Note(default_x=125.76, default_y=-140.92):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=125.76, default_y=-130.92):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=188.6, default_y=-135.92):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=188.6, default_y=-125.92):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='115', width=186.0):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=94.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=126.94, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=61.37, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=61.37, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=94.16, default_y=-110.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=126.94, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=126.94, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='116', width=211.08):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=117.5, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=128.47, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=139.43, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=150.4, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=162.12, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=185.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('legato', default_y=-40.0, relative_x=25.33, relative_y=-37.67, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.48, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.38, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.06, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.75, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.43, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.12, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='117', width=223.56):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=61.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=171.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.27, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=61.93, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.2, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.47, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.73, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.43, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.7, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='118', width=195.43):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=58.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=103.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=148.26, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=170.66, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.21, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.62, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.03, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=103.44, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.85, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.26, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.66, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='119', width=240.42):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=94.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=110.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=137.11, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.23, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.12, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.55, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=137.11, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=162.54, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.96, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.39, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='120', width=300.97):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(97.29)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=63.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=195.94, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=206.9, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=217.87, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=228.83, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=240.55, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=269.96, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=63.6, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.01, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=122.91, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.32, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=181.73, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.14, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=240.55, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=269.96, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='121', width=239.64):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=152.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=181.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=209.53, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.5, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.01, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.51, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=124.02, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.52, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.03, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.53, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='122', width=277.32):
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=46.54, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=79.28, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=112.02, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=144.76, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=177.5, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=210.24, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=242.98, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.54, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.28, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.02, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=144.76, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.5, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.24, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.98, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='123', width=238.57):
            with Note(default_x=21.03, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=129.0, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=21.03, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.02, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.02, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.01, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=129.0, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.99, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=182.98, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.98, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='124', width=397.99):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(97.29)
                with StaffLayout(number=2):
                    StaffDistance(72.88)
            with Note(default_x=71.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=151.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=177.77, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=204.34, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=237.0, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=263.57, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=290.13, default_y=-5.0):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='stop')
            with Note(default_x=316.7, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=343.26, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=369.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=71.52, default_y=-137.88):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=98.08, default_y=-127.88):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.64, default_y=-117.88):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=151.21, default_y=-102.88):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='125', width=313.6):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=110.67, default_y=-15.0):
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
            with Note(default_x=135.83, default_y=0.0):
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
            with Note(default_x=161.0, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=186.16, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.33, default_y=-15.0):
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
                    Tuplet(type='stop')
            with Note(default_x=236.5, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=261.66, default_y=-15.0):
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
            with Note(default_x=286.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-157.88):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
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
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=35.17, default_y=-147.88):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.33, default_y=-137.88):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=85.5, default_y=-122.88):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='126', width=344.91):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=94.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=124.5, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.85, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=179.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=206.55, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=233.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
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
                    Tuplet(type='stop')
            with Note(default_x=261.25, default_y=-5.0):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=288.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
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
            with Note(default_x=315.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-147.88):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.9, default_y=-137.88):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.25, default_y=-127.88):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=94.6, default_y=-112.88):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='127', width=329.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(97.29)
                with StaffLayout(number=2):
                    StaffDistance(73.92)
            with Note(default_x=72.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=140.66, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=159.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
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
            with Note(default_x=179.08, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=208.98, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=228.19, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=247.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
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
                    Tuplet(type='stop')
            with Note(default_x=266.6, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=285.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
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
            with Note(default_x=305.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=72.35, default_y=-133.92):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=102.25, default_y=-123.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.46, default_y=-113.92):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=140.66, default_y=-98.92):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='128', width=252.23):
            with Note(default_x=14.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=70.04, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=88.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Note(default_x=107.4, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=134.06, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
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
            with Note(default_x=152.74, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=171.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
                    Tuplet(type='stop')
            with Note(default_x=190.1, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=208.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Note(default_x=227.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=14.0, default_y=-143.92):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=32.68, default_y=-133.92):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.36, default_y=-118.92):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=70.04, default_y=-108.92):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='129', width=236.13):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=64.92, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=83.22, default_y=-30.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=101.53, default_y=-15.0):
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
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=119.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
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
            with Note(default_x=138.14, default_y=-15.0):
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
            with Note(default_x=156.45, default_y=-30.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='stop')
            with Note(default_x=174.75, default_y=-15.0):
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=193.06, default_y=-30.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=211.36, default_y=-40.0):
                with Pitch():
                    Step('E')
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-138.92):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=28.31, default_y=-128.92):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=46.61, default_y=-118.92):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=64.92, default_y=-103.92):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='130', width=238.35):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=29.47, default_y=-45.0):
                with Pitch():
                    Step('D')
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
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=47.88, default_y=-25.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='stop')
            with Note(default_x=66.29, default_y=-10.0):
                with Pitch():
                    Step('D')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=84.7, default_y=-25.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=103.11, default_y=-45.0):
                with Pitch():
                    Step('D')
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
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=139.94, default_y=-45.0):
                with Pitch():
                    Step('D')
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
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=158.35, default_y=-25.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='stop')
            with Note(default_x=176.76, default_y=-15.0):
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=195.17, default_y=-25.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=213.58, default_y=-45.0):
                with Pitch():
                    Step('D')
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=11.06, default_y=-123.92):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=11.06, default_y=-113.92):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=121.52, default_y=-123.92):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=121.52, default_y=-113.92):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='131', width=257.66):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(97.29)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=63.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=182.96, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=209.63, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=232.89, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=63.6, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.97, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.86, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.23, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=160.6, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=182.96, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.63, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=232.89, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='132', width=192.65):
            with Note(default_x=13.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=99.84, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=123.1, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.37, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.88, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.31, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.82, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.33, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=99.84, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.1, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.37, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.88, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='133', width=167.95):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=86.1, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=124.15, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.03, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.05, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.08, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=86.1, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=105.13, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.15, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.18, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='134', width=190.83):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=66.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=17.23, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=37.05, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.95, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.77, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.6, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=126.42, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.24, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.07, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='135', width=247.41):
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=89.41, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=122.07, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=154.14, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=188.61, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
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
            with Note(default_x=220.68, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
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
                Duration(48.0)
            with Note(default_x=14.0, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.14, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.27, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.41, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=122.07, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=154.14, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.61, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.68, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='136', width=237.42):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(97.29)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=63.6, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=145.62, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=168.89, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.15, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.66, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=63.6, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=84.1, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.61, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.11, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=145.62, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.89, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.15, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.66, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='137', width=162.92):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=28.31, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=46.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=83.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=119.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=28.31, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=46.62, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=64.92, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=83.23, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.54, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.85, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.16, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='138', width=200.67):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=93.73, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=129.38, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=152.64, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=175.91, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('legato', default_y=-40.0, relative_x=25.33, relative_y=-37.67, font_style='italic', font_size='11')
                Staff(2)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.78, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.76, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.75, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.73, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.71, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.64, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.91, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='139', width=219.37):
            with Note(default_x=13.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=110.92, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=148.08, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=171.34, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=194.61, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.29, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.77, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.26, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.92, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.41, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.34, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.61, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='140', width=236.1):
            with Note(default_x=13.8, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=131.3, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=168.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=188.07, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=211.34, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.44, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.08, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.72, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=131.3, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.94, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.07, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.34, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='141', width=268.39):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=64.11, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=89.03, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=113.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.86, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=163.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=216.96, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=64.11, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=89.03, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=113.94, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.86, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=163.78, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=188.69, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.96, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.87, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='142', width=192.57):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=52.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=94.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=131.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=146.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=167.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.08, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.16, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.24, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=94.32, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=115.4, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.73, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.81, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='143', width=207.09):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=106.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=144.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=159.9, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=182.33, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.43, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.85, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.28, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.14, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=128.57, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.9, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=182.33, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='144', width=205.11):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=99.56, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=137.62, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('forward hook', number=3)
            with Note(default_x=157.08, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.35, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.39, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.78, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.17, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=99.56, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.95, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.08, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.35, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='145', width=183.32):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=34.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=55.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=75.84, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=96.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=117.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=137.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=158.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.48, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.16, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.84, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=96.52, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=117.2, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.88, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.56, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='146', width=288.78):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(95.18)
                with StaffLayout(number=2):
                    StaffDistance(67.17)
            with Note(default_x=61.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=101.2, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=121.55, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=141.9, default_y=-15.0):
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
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=162.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=182.6, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=202.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
                    Tuplet(type='stop')
            with Note(default_x=223.31, default_y=-15.0):
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=243.66, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=264.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=101.2, default_y=-132.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=101.2, default_y=-122.17):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=162.25, default_y=-127.17):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=162.25, default_y=-117.17):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=223.31, default_y=-122.17):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=223.31, default_y=-112.17):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='147', width=265.16):
            with Note(default_x=10.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=74.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Note(default_x=96.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=126.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=148.18, default_y=-25.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=170.03, default_y=-45.0):
                with Pitch():
                    Step('D')
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
                    Tuplet(type='stop')
            with Note(default_x=196.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=218.54, default_y=-30.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=240.39, default_y=-45.0):
                with Pitch():
                    Step('D')
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=52.74, default_y=-147.17):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=52.74, default_y=-137.17):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=126.34, default_y=-142.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=126.34, default_y=-132.17):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=196.7, default_y=-137.17):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=196.7, default_y=-127.17):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='148', width=237.4):
            with Note(default_x=10.12, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=49.82, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=70.18, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=90.53, default_y=-15.0):
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
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=110.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
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
            with Note(default_x=131.23, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=151.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
                    Tuplet(type='stop')
            with Note(default_x=171.93, default_y=-15.0):
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=192.29, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=212.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=49.82, default_y=-132.17):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=49.82, default_y=-122.17):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=110.88, default_y=-127.17):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=110.88, default_y=-117.17):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=171.93, default_y=-122.17):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=171.93, default_y=-112.17):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='149', width=265.16):
            with Note(default_x=10.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
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
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=74.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
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
            with Note(default_x=96.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=126.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=148.18, default_y=-25.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=170.03, default_y=-45.0):
                with Pitch():
                    Step('D')
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
                    Tuplet(type='stop')
            with Note(default_x=196.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=218.54, default_y=-30.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=240.39, default_y=-45.0):
                with Pitch():
                    Step('D')
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=52.74, default_y=-147.17):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=52.74, default_y=-137.17):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=126.34, default_y=-142.17):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=126.34, default_y=-132.17):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=196.7, default_y=-137.17):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=196.7, default_y=-127.17):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
        with Measure(number='150', width=311.51):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(95.18)
                with StaffLayout(number=2):
                    StaffDistance(75.14)
            with Note(default_x=61.37, default_y=-40.0):
                with Pitch():
                    Step('E')
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=81.86, default_y=-50.0):
                with Pitch():
                    Step('C')
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
            with Note(default_x=102.35, default_y=-40.0):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='stop')
            with Note(default_x=122.84, default_y=-30.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=143.33, default_y=-40.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=163.82, default_y=-30.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=184.3, default_y=-15.0):
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
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=204.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=225.28, default_y=-15.0):
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
                    Tuplet(type='stop')
            with Note(default_x=245.77, default_y=-5.0):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=266.26, default_y=-15.0):
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
            with Note(default_x=286.75, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Backup():
                Duration(48.0)
            with Note(default_x=61.37, default_y=-140.14):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='151', width=317.36):
            with Note(default_x=14.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=37.51, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=60.86, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='stop')
            with Note(default_x=93.53, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=116.88, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=140.23, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=163.59, default_y=-15.0):
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
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=192.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.8, default_y=-30.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='stop')
            with Note(default_x=239.16, default_y=-15.0):
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=262.51, default_y=-25.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=292.4, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-140.14):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-105.14):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(48.0)
            with Note(default_x=14.52, default_y=-120.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(36.0)
                Voice('7')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=239.16, default_y=-110.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
        with Measure(number='152', width=233.34):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=40.43, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=71.94, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=98.57, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=125.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=151.84, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.47, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=205.1, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-125.14):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-115.14):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-105.14):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='153', width=194.29):
            with Note(default_x=10.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(36.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=138.99, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=165.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Forward():
                Duration(36.0)
            with Note(default_x=138.99, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=53.08, default_y=-125.14):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=96.03, default_y=-120.14):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=53.08, default_y=-95.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=96.03, default_y=-95.14):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=138.99, default_y=-90.14):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='154', width=311.62):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(95.18)
                with StaffLayout(number=2):
                    StaffDistance(80.09)
            with Note(default_x=61.37, default_y=-15.0):
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
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=81.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
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
            with Note(default_x=101.14, default_y=-15.0):
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
                    Tuplet(type='stop')
            with Note(default_x=121.02, default_y=-5.0):
                with Pitch():
                    Step('E')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=140.91, default_y=-15.0):
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
            with Note(default_x=160.79, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=180.67, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
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
            with Note(default_x=200.56, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=220.44, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='stop')
            with Note(default_x=240.33, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=263.59, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
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
            with Note(default_x=286.86, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
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
            with Backup():
                Duration(48.0)
            with Note(default_x=61.37, default_y=-110.09):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=61.37, default_y=-100.09):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='155', width=292.06):
            with Note(default_x=20.0, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=43.27, default_y=10.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=63.92, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='stop')
            with Note(default_x=84.58, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=105.24, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=125.9, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=146.56, default_y=-15.0):
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
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=167.22, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=187.88, default_y=-15.0):
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
                    Tuplet(type='stop')
            with Note(default_x=216.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=237.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
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
            with Note(default_x=267.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
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
                Duration(48.0)
            with Note(default_x=19.64, default_y=-145.09):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(48.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(48.0)
            with Note(default_x=19.64, default_y=-110.09):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(48.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(48.0)
            with Note(default_x=20.36, default_y=-125.09):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(36.0)
                Voice('7')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=216.74, default_y=-115.09):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('7')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
        with Measure(number='156', width=212.55):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=37.46, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=68.97, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.63, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=116.29, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.96, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.62, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.28, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-130.09):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-120.09):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-110.09):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='157', width=240.26):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Note(default_x=46.66, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=78.72, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.38, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=132.04, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=158.69, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.35, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.0, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(48.0)
            with Note(default_x=20.0, default_y=-130.09):
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
            with Note(default_x=20.0, default_y=-100.09):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='158', width=246.16):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(95.18)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=63.6, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=86.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=108.68, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=131.22, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=153.77, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=176.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=198.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=221.39, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=63.6, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=86.14, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.68, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.22, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=153.77, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=176.31, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.85, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.39, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='159', width=201.05):
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=97.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=160.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=176.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.77, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.75, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.72, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.7, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=118.67, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.64, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.62, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='160', width=232.02):
            with Note(default_x=44.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=128.67, default_y=-30.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=173.15, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=191.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=207.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(48.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-2.67, relative_y=25.33):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=44.77, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=65.75, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.72, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.69, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=128.67, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=149.64, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.62, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.59, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='161', width=180.02):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=51.5, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=134.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.75, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.5, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.25, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.75, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.5, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.25, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='162', width=197.25):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=93.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=138.38, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=156.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=172.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.97, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.95, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.92, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.9, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=114.87, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.84, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.82, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='163', width=268.41):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(95.18)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=112.73, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=164.09, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=215.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(48.0)
            with Note(default_x=61.37, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=87.05, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.73, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.41, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=164.09, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=189.77, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.45, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.13, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='164', width=251.5):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=97.49, default_y=-30.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=115.95, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=195.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('32nd')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=211.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
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
            with Note(default_x=226.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
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
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.49, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.97, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.46, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=115.95, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.43, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.92, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.41, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='165', width=242.63):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=97.03, default_y=-30.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('32nd')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=115.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(18.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=194.6, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=217.87, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.37, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.74, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.11, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=115.49, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.86, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.23, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.6, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='166', width=293.95):
            with Note(default_x=13.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=132.41, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=156.73, default_y=10.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=188.06, default_y=5.0):
                with Pitch():
                    Step('G')
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
                    Tuplet(type='stop')
            with Note(default_x=212.38, default_y=0.0):
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
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=236.7, default_y=-5.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=268.03, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=43.45, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.11, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.76, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=132.41, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=172.4, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.38, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.36, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='167', width=371.85):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=61.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=190.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=216.79, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=249.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=276.28, default_y=10.0):
                with Pitch():
                    Step('A')
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
                    Tuplet(type='start', bracket='no')
            with Note(default_x=310.76, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=343.81, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
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
                Duration(48.0)
            with Note(default_x=61.37, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.62, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.86, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.1, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=190.34, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=233.31, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.28, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.28, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='168', width=197.38):
            with Note(default_x=13.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=55.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('16th')
                Dot()
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=92.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('backward hook', number=3)
            with Note(default_x=111.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=153.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=153.87, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=153.87, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='169', width=149.79):
            with Note(default_x=10.0, default_y=-35.0):
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
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=10.0, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=71.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=71.42, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=10.0, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(36.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='170', width=174.87):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=93.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=93.53, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=105.4, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=93.53, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=26.67, relative_y=30.67):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=13.8, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
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
            with Note(default_x=93.53, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=93.53, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
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
        with Measure(number='171', width=162.59):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(24.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(48.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
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
            with Note():
                Rest()
                Duration(24.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')