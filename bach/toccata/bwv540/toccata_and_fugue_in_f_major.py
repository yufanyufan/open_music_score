with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Ellipsis')
    with Identification():
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
        CreditWords('Ellipsis', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(49)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=223.0):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(401.95)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(118.25)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
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
            with Harmony(print_frame='no'):
                Function('V7')
                Kind('none', text='')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Example from the textbook "Harmony"\n', relative_x=-37.82, relative_y=45.22)
                    Words('by Dubovsky, Evseev, Sposobin, Sokolov (1984 edition, page 429):\n')
                    Words(None)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('C:', default_y=-40.0, relative_x=-23.11, relative_y=-31.97)
                Staff(1)
            with Note(default_x=82.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=100.93, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=82.43, default_y=-163.25):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=82.43, default_y=-153.25):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='2', width=173.57):
            with Harmony(print_frame='no'):
                Function('V2')
                Kind('none', text='')
            with Direction(placement='below'):
                with DirectionType():
                    Words('D♭:', default_y=-40.0, relative_x=-32.57, relative_y=-31.02)
                Staff(1)
            with Note(default_x=55.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Accidental('flat')
                Staff(1)
            with Note(default_x=55.21, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Accidental('flat')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=55.21, default_y=-163.25):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
            with Note(default_x=55.21, default_y=-148.25):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='3', width=278.98):
            with Harmony(print_frame='no'):
                Function('I6')
                Kind('none', text='')
            with Harmony(print_frame='no'):
                Function('♭II6')
                Kind('none', text='')
            with Direction(placement='below'):
                with DirectionType():
                    Words('D♭:', default_y=-40.0, relative_x=-33.62, relative_y=-33.12)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('=', default_y=-40.0, relative_x=45.18, relative_y=-35.52, font_size='15')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('C:', default_y=-40.0, relative_x=76.7, relative_y=-33.02)
                Staff(1)
            with Note(default_x=53.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Accidental('flat')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        BreathMark(None)
            with Note(default_x=53.32, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Accidental('flat')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Neapolitan sixth\n', relative_x=70.39, relative_y=63.46)
                    Words('chord in C major\n')
                    Words(None)
                Staff(2)
            with Note(default_x=53.32, default_y=-168.25):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=53.32, default_y=-143.25):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
        with Measure(number='4', width=370.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(127.42)
            with Attributes():
                with Key():
                    Fifths(-1)
                with Time():
                    Beats('3')
                    BeatType('8')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-35.06, default_y=21.8, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Bach, Toccata in F major, BWV 540, mm. 423-425', relative_y=20.0)
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=190.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                Function('V7')
                Kind('none', text='')
            with Direction(placement='below'):
                with DirectionType():
                    Words('F:', default_y=-40.0, relative_x=-21.01, relative_y=-61.96)
                Staff(1)
            with Note(default_x=290.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=190.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=279.7, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(6.0)
            with Forward():
                Duration(2.0)
            with Note(default_x=190.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=290.86, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(6.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=194.37, default_y=-192.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=284.0, default_y=-227.42):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Staff(2)
            with Note(default_x=190.07, default_y=-172.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=279.7, default_y=-172.42):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=100.44, default_y=-192.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('8')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('8')
                Type('eighth')
                Staff(2)
        with Measure(number='5', width=355.49):
            with Harmony(print_frame='no'):
                Function('V2')
                Kind('none', text='')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G♭:', default_y=-40.0, relative_x=-38.2, relative_y=-58.05)
                Staff(1)
            with Note(default_x=51.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=51.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(print_object='no'):
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=101.48, default_y=-187.42):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=151.96, default_y=-177.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.44, default_y=-187.42):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.93, default_y=-167.42):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=303.41, default_y=-177.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(6.0)
            with Note(default_x=51.0, default_y=-177.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=51.0, default_y=-167.42):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(4.0)
            with Note(print_object='no'):
                Rest()
                Duration(4.0)
                Voice('7')
                Type('quarter')
                Staff(2)
            with Note(print_object='no'):
                Rest()
                Duration(2.0)
                Voice('7')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=51.0, default_y=-192.42):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('8')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('8')
                Type('eighth')
                Staff(2)
        with Measure(number='6', width=330.08):
            with Harmony(print_frame='no'):
                Function('I6')
                Kind('none', text='')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('G♭:', default_y=-40.0, relative_x=-54.44, relative_y=-60.34)
                Staff(1)
            with Note(default_x=69.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=119.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.74, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=269.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(6.0)
            with Note(default_x=20.0, default_y=-152.42):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=20.0, default_y=-197.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('8')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('8')
                Type('eighth')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')