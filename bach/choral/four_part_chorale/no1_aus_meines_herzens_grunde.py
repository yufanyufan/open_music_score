with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Aus meines Herzens Grunde')
    with Identification():
        Creator('Johann Sebastian Bach', type='composer')
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
            PageHeight(1584.0)
            PageWidth(1224.0)
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
        CreditWords('Aus meines Herzens Grunde', default_x=612.0, default_y=1527.31, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('(Choral 1, "Vierstimmige Choralgesänge", Breitkopf & Härtel)\n', default_x=612.0, default_y=1470.61, justify='center', valign='top', font_size='14')
        CreditWords('\n')
        CreditWords(None)
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J. S. Bach\n', default_x=1167.31, default_y=1351.99, justify='right', valign='bottom', font_size='12')
        CreditWords('\n')
        CreditWords('Analysis by S. Shchetnikov\n')
        CreditWords(None)
    with PartList():
        with ScorePart(id='P1'):
            PartName('Pipe Organ')
            PartAbbreviation('Org.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Pipe Organ')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(20)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=168.46):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(245.31)
                with StaffLayout(number=2):
                    StaffDistance(115.72)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(1)
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
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('90')
                Staff(1)
                Sound(tempo=90.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('G:', default_y=-40.0, relative_x=-42.86, relative_y=-41.08)
                Staff(1)
            with Note(default_x=100.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=100.67, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=100.67, default_y=-150.72):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(2.0)
            with Note(default_x=100.67, default_y=-195.72):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='1', width=299.99):
            with Harmony(print_frame='no'):
                Function('IV6')
                Kind('none', text='')
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Harmony(print_frame='no'):
                Function('V6')
                Kind('none', text='')
            with Note(default_x=210.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=100.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=210.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-150.72):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=100.37, default_y=-145.72):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                Function('vi')
                Kind('none', text='')
            with Note(default_x=155.38, default_y=-150.72):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=210.38, default_y=-155.72):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-160.72):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=100.37, default_y=-170.72):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=210.38, default_y=-165.72):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='2', width=252.04):
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Note(default_x=12.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Harmony(print_frame='no'):
                Function('V')
                Kind('none', text='')
            with Note(default_x=85.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#FF00FF')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=131.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Harmony(print_frame='no'):
                Function('vi')
                Kind('none', text='')
            with Note(default_x=177.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=177.29, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.72, default_y=-160.72):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=85.87, default_y=-165.72):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=177.29, default_y=-160.72):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.72, default_y=-160.72):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=85.87, default_y=-175.72):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=177.29, default_y=-170.72):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=369.12):
            with Harmony(print_frame='no'):
                Function('IV')
                Kind('none', text='')
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Harmony(print_frame='no'):
                Function('viio6')
                Kind('none', text='')
            with Note(default_x=197.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Note(default_x=270.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=76.33, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=136.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=197.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=270.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-145.72):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=76.33, default_y=-150.72):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=136.86, default_y=-145.72):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=270.67, default_y=-140.72):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-180.72):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=136.86, default_y=-185.72):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#42AAFF')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=197.4, default_y=-190.72):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=270.67, default_y=-195.72):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=330.55):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(95.84)
                with StaffLayout(number=2):
                    StaffDistance(119.57)
            with Harmony(print_frame='no'):
                Function('V')
                Kind('none', text='')
            with Note(default_x=79.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Note(default_x=233.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=233.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.61, default_y=-144.57):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-10.0)
            with Note(default_x=233.19, default_y=-144.57):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.61, default_y=-179.57):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=233.19, default_y=-199.57):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=277.0):
            with Harmony(print_frame='no'):
                Function('IV6')
                Kind('none', text='')
            with Harmony(print_frame='no'):
                Function('vi65')
                Kind('none', text='')
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Harmony(print_frame='no'):
                Function('viio6')
                Kind('none', text='')
            with Note(default_x=187.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=100.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=187.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-159.57):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=100.04, default_y=-154.57):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=187.72, default_y=-149.57):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-204.57):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=100.04, default_y=-199.57):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=187.72, default_y=-194.57):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=319.47):
            with Harmony(print_frame='no'):
                Function('I6')
                Kind('none', text='')
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Harmony(print_frame='no'):
                Function('ii65')
                Kind('none', text='')
            with Harmony(print_frame='no'):
                Function('V')
                Kind('none', text='')
            with Note(default_x=108.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=201.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-144.57):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=108.74, default_y=-139.57):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=201.69, default_y=-144.57):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                Function('V7')
                Kind('none', text='')
            with Note(default_x=259.78, default_y=-149.57):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-189.57):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=108.74, default_y=-184.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=201.69, default_y=-179.57):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=162.6):
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Note(default_x=12.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(4.0)
            with Note(default_x=12.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(4.0)
            with Note(default_x=12.36, default_y=-154.57):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(4.0)
            with Note(default_x=12.36, default_y=-199.57):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-30.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='8', width=191.77):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(95.84)
                with StaffLayout(number=2):
                    StaffDistance(125.46)
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Note(default_x=79.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2.0)
            with Note(default_x=79.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(2.0)
            with Note(default_x=79.61, default_y=-150.46):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(2.0)
            with Note(default_x=79.61, default_y=-205.46):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='9', width=497.82):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Harmony(print_frame='no'):
                Function('ii')
                Kind('none', text='')
            with Harmony(print_frame='no'):
                Function('viio6')
                Kind('none', text='')
            with Note(default_x=175.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Harmony(print_frame='no'):
                Function('I6')
                Kind('none', text='')
            with Note(default_x=336.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=95.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#42AAFF')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=175.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=256.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=336.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-150.46):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=175.94, default_y=-155.46):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=336.08, default_y=-160.46):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=416.15, default_y=-165.46):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#00AA00')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-205.46):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=175.94, default_y=-200.46):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=336.08, default_y=-195.46):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=400.02):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Harmony(print_frame='no'):
                Function('V43')
                Kind('none', text='')
            with Note(default_x=219.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Note(default_x=288.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=81.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=150.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=219.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=288.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.0, default_y=-160.46):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=81.0, default_y=-155.46):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Notehead('normal', color='#42AAFF')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=150.01, default_y=-150.46):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=288.02, default_y=-150.46):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.0, default_y=-195.46):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=219.01, default_y=-200.46):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=288.02, default_y=-205.46):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=379.62):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(95.84)
                with StaffLayout(number=2):
                    StaffDistance(130.33)
            with Harmony(print_frame='no'):
                Function('V')
                Kind('none', text='')
            with Note(default_x=79.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Harmony(print_frame='no'):
                Function('vi')
                Kind('none', text='')
            with Note(default_x=263.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=263.39, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.61, default_y=-155.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=263.39, default_y=-165.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.61, default_y=-190.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-10.0)
            with Note(default_x=263.39, default_y=-185.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='12', width=344.09):
            with Harmony(print_frame='no'):
                Function('iii6')
                Kind('none', text='')
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Harmony(print_frame='no'):
                Function('ii6')
                Kind('none', text='')
            with Note(default_x=240.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=113.94, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=177.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#42AAFF')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=240.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-175.33):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=113.94, default_y=-165.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=240.91, default_y=-150.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-185.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=113.94, default_y=-190.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=240.91, default_y=-195.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=365.9):
            with Harmony(print_frame='no'):
                Function('I6')
                Kind('none', text='')
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Harmony(print_frame='no'):
                Function('V7')
                Kind('none', text='')
            with Note(default_x=239.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=16.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF00FF')
                Staff(1)
            with Note(default_x=115.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=239.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF00FF')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=302.13, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-155.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=239.97, default_y=-155.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=16.16, default_y=-200.33):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=177.8, default_y=-195.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#42AAFF')
                Staff(2)
            with Note(default_x=239.97, default_y=-190.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='14', width=411.16):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(114.74)
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Harmony(print_frame='no'):
                Function('I6')
                Kind('none', text='')
            with Harmony(print_frame='no'):
                Function('V7')
                Kind('none', text='')
            with Note(default_x=79.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('C:', default_y=-40.0, relative_x=-29.81, relative_y=-37.65)
                Staff(1)
            with Note(default_x=308.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.61, default_y=-139.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.97, default_y=-194.74):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=143.36, default_y=-189.74):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#42AAFF')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=206.74, default_y=-184.74):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=308.15, default_y=-194.74):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=310.41):
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Direction(placement='below'):
                with DirectionType():
                    Words('G:', default_y=-40.0, relative_x=-43.83, relative_y=-39.81)
                Staff(1)
            with Note(default_x=196.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=196.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-144.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=196.25, default_y=-139.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-179.74):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-10.0)
            with Note(default_x=196.25, default_y=-194.74):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=368.05):
            with Harmony(print_frame='no'):
                Function('V6')
                Kind('none', text='')
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Note(default_x=15.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Harmony(print_frame='no'):
                Function('viio6')
                Kind('none', text='')
            with Note(default_x=266.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=141.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF00FF')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=203.65, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=266.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-139.74):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                Function('V65')
                Kind('none', text='')
            with Note(default_x=78.42, default_y=-144.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=141.03, default_y=-149.74):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=266.26, default_y=-144.74):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-199.74):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=141.03, default_y=-194.74):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=266.26, default_y=-189.74):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=390.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(126.43)
            with Harmony(print_frame='no'):
                Function('I6')
                Kind('none', text='')
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Note(default_x=79.61, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Harmony(print_frame='no'):
                Function('V')
                Kind('none', text='')
            with Note(default_x=270.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=270.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(6.0)
            with Note(default_x=79.61, default_y=-151.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=270.24, default_y=-151.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                Function('V7')
                Kind('none', text='')
            with Note(default_x=329.7, default_y=-156.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.97, default_y=-196.43):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=175.11, default_y=-206.43):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=270.24, default_y=-186.43):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=408.36):
            with Harmony(print_frame='no'):
                Function('vi')
                Kind('none', text='')
            with Harmony(print_frame='no'):
                Function('IV')
                Kind('none', text='')
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Harmony(print_frame='no'):
                Function('viio6')
                Kind('none', text='')
            with Note(default_x=209.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Note(default_x=275.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=32.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#FF00FF')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=77.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=143.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=209.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=275.17, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.0, default_y=-161.43):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=143.59, default_y=-156.43):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('cf. m3', relative_x=-86.04, relative_y=24.68)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='start', number=1, line_end='none', line_type='solid', default_y=58.51, relative_x=-51.43)
                Staff(2)
            with Note(default_x=275.17, default_y=-151.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Bracket(type='stop', number=1, line_end='none', relative_x=-125.36)
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.0, default_y=-181.43):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=77.79, default_y=-186.43):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#42AAFF')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=143.59, default_y=-191.43):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=209.38, default_y=-196.43):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#42AAFF')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=275.17, default_y=-201.43):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#42AAFF')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=340.97, default_y=-206.43):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='19', width=290.5):
            with Harmony(print_frame='no'):
                Function('V')
                Kind('none', text='')
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Note(default_x=184.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=184.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-151.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=184.0, default_y=-151.43):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-186.43):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-10.0)
            with Note(default_x=184.0, default_y=-171.43):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='20', width=407.25):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(123.22)
            with Harmony(print_frame='no'):
                Function('V6')
                Kind('none', text='')
            with Note(default_x=79.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Harmony(print_frame='no'):
                Function('IV6')
                Kind('none', text='')
            with Note(default_x=280.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=280.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=343.02, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#00AA00')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.61, default_y=-148.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=280.39, default_y=-143.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=79.97, default_y=-168.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Notehead('normal', color='#FF00FF')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=180.18, default_y=-173.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=280.39, default_y=-178.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=371.02):
            with Harmony(print_frame='no'):
                Function('vi')
                Kind('none', text='')
            with Note(default_x=16.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Harmony(print_frame='no'):
                Function('ii65')
                Kind('none', text='')
            with Harmony(print_frame='no'):
                Function('V')
                Kind('none', text='')
            with Note(default_x=141.97, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=243.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=15.8, default_y=-143.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=243.26, default_y=-148.22):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Harmony(print_frame='no'):
                Function('V7')
                Kind('none', text='')
            with Note(default_x=306.34, default_y=-153.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(6.0)
            with Note(default_x=16.16, default_y=-178.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=79.24, default_y=-183.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Notehead('normal', color='#42AAFF')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=142.33, default_y=-188.22):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=243.26, default_y=-183.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='22', width=311.34):
            with Harmony(print_frame='no'):
                Function('I')
                Kind('none', text='')
            with Note(default_x=12.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-158.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(6.0)
            with Note(default_x=12.36, default_y=-203.22):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-30.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('6')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')